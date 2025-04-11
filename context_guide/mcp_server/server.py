"""
Implementação do servidor MCP (Model Control Panel) para fornecer contexto ao Cursor IDE.
Utiliza FastAPI para criar endpoints RESTful para consulta de contexto.
"""

import logging
import os
import time
import json
from datetime import datetime
from typing import Dict, Any, Optional, List
from fastapi import FastAPI, HTTPException, Body, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn

from context_guide.context import ContextManager
from context_guide.prompt_generator import PromptGenerator

# Configuração de logging avançada
log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
log_level = os.environ.get('CONTEXT_GUIDE_LOG_LEVEL', 'INFO')
log_file = os.environ.get('CONTEXT_GUIDE_LOG_FILE', None)

# Configurar logger raiz
logging.basicConfig(
    level=getattr(logging, log_level),
    format=log_format,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(log_file) if log_file else logging.NullHandler()
    ]
)
logger = logging.getLogger(__name__)

# Modelos de dados
class ContextRequest(BaseModel):
    """Modelo para requisições de contexto."""
    query: str
    num_results: int = 5
    technology_context: Optional[str] = None

class PromptRequest(BaseModel):
    """Modelo para requisições de geração de prompt."""
    request: str
    technology_context: Optional[str] = None
    include_best_practices: bool = True

class ContextResponse(BaseModel):
    """Modelo para respostas com contexto."""
    context: str
    sources: List[Dict[str, Any]]
    retrieval_time: Optional[float] = None

class PromptResponse(BaseModel):
    """Modelo para respostas com prompt."""
    prompt: str
    generation_time: Optional[float] = None

class ServerStatsResponse(BaseModel):
    """Modelo para estatísticas do servidor."""
    uptime: float
    total_requests: int
    context_requests: int
    prompt_requests: int
    update_requests: int
    avg_response_time: float

# Métricas do servidor
server_metrics = {
    "start_time": time.time(),
    "total_requests": 0,
    "context_requests": 0,
    "prompt_requests": 0, 
    "update_requests": 0,
    "response_times": []
}

# Criar a aplicação FastAPI
app = FastAPI(
    title="Context Guide MCP Server",
    description="Serviço de API para fornecer contexto de documentação para o Cursor IDE",
    version="0.1.0"
)

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, isso deve ser restrito aos domínios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware para métricas
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    """Middleware para coletar métricas de requisições."""
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    
    # Atualizar métricas
    server_metrics["total_requests"] += 1
    server_metrics["response_times"].append(process_time)
    
    # Registrar endpoint específico
    endpoint = request.url.path
    if endpoint == "/context":
        server_metrics["context_requests"] += 1
    elif endpoint == "/prompt":
        server_metrics["prompt_requests"] += 1
    elif endpoint == "/update-index":
        server_metrics["update_requests"] += 1
    
    # Registrar no log
    logger.info(f"Requisição para {endpoint} completada em {process_time:.4f}s")
    
    return response

# Estado compartilhado para a aplicação
context_manager = None
prompt_generator = None

@app.on_event("startup")
async def startup_event():
    """Inicializar serviços na inicialização do servidor."""
    global context_manager, prompt_generator
    
    # Obter configurações do ambiente ou usar valores padrão
    docs_dir = os.environ.get("CONTEXT_GUIDE_DOCS_DIR", "docs")
    db_dir = os.environ.get("CONTEXT_GUIDE_DB_DIR", ".context_guide")
    
    try:
        logger.info(f"Inicializando ContextManager com documentos em '{docs_dir}' e DB em '{db_dir}'")
        context_manager = ContextManager(docs_dir=docs_dir, db_dir=db_dir)
        prompt_generator = PromptGenerator(context_manager)
        logger.info("Servidor MCP inicializado com sucesso")
    except Exception as e:
        logger.error(f"Erro ao inicializar servidor MCP: {e}")
        raise e

@app.get("/")
async def root():
    """Endpoint raiz para verificar se o serviço está rodando."""
    return {
        "status": "online", 
        "service": "Context Guide MCP Server",
        "timestamp": datetime.now().isoformat(),
        "version": "0.1.0"
    }

@app.post("/context", response_model=ContextResponse)
async def get_context(request: ContextRequest):
    """
    Endpoint para obter contexto relevante para uma consulta.
    
    Args:
        request: Modelo com a consulta e número de resultados desejados
        
    Returns:
        ContextResponse com o contexto e fontes encontradas
    """
    if not context_manager:
        raise HTTPException(status_code=503, detail="Serviço não inicializado corretamente")
    
    try:
        start_time = time.time()
        tech_context = request.technology_context
        
        if tech_context:
            logger.info(f"Recebida consulta com contexto de tecnologia '{tech_context}': '{request.query}'")
            # Ajustar a consulta para incluir o contexto tecnológico
            enhanced_query = f"{request.query} (em contexto de {tech_context})"
        else:
            logger.info(f"Recebida consulta: '{request.query}'")
            enhanced_query = request.query
            
        result = context_manager.get_relevant_context(enhanced_query, request.num_results)
        
        # Adicionar tempo de processamento
        retrieval_time = time.time() - start_time
        result["retrieval_time"] = retrieval_time
        
        logger.info(f"Consulta processada em {retrieval_time:.4f}s, retornado {len(result.get('sources', []))} fontes")
        return result
    except Exception as e:
        logger.error(f"Erro ao processar consulta: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/prompt", response_model=PromptResponse)
async def generate_prompt(request: PromptRequest):
    """
    Endpoint para gerar um prompt enriquecido com contexto.
    
    Args:
        request: Modelo com a solicitação do usuário
        
    Returns:
        PromptResponse com o prompt gerado
    """
    if not prompt_generator:
        raise HTTPException(status_code=503, detail="Serviço não inicializado corretamente")
    
    try:
        start_time = time.time()
        
        # Adicionar informações de tecnologia e práticas, se disponíveis
        user_request = request.request
        if request.technology_context:
            tech_info = f" (tecnologia: {request.technology_context})"
            user_request += tech_info
            logger.info(f"Gerando prompt para '{request.request}' com tecnologia '{request.technology_context}'")
        else:
            logger.info(f"Gerando prompt para: '{request.request}'")
        
        prompt = prompt_generator.generate_prompt(user_request)
        
        # Adicionar melhores práticas se solicitado
        if request.include_best_practices:
            prompt += "\n\n## Melhores Práticas a Considerar\n"
            prompt += "- Garantir que o código seja testável e mantenha princípios SOLID\n"
            prompt += "- Incluir tratamento de erros apropriado\n"
            prompt += "- Seguir os padrões de estilo e nomenclatura do projeto\n"
            prompt += "- Implementar logging adequado para facilitar depuração\n"
        
        generation_time = time.time() - start_time
        
        logger.info(f"Prompt gerado em {generation_time:.4f}s com {len(prompt)} caracteres")
        return {"prompt": prompt, "generation_time": generation_time}
    except Exception as e:
        logger.error(f"Erro ao gerar prompt: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/update-index")
async def update_index():
    """
    Endpoint para atualizar o índice de documentos.
    
    Returns:
        Dict com status da operação
    """
    if not context_manager:
        raise HTTPException(status_code=503, detail="Serviço não inicializado corretamente")
    
    try:
        start_time = time.time()
        logger.info("Iniciando atualização do índice de documentos")
        
        context_manager.update_index()
        
        update_time = time.time() - start_time
        logger.info(f"Índice atualizado com sucesso em {update_time:.2f}s")
        
        return {
            "status": "success", 
            "message": "Índice atualizado com sucesso",
            "update_time": update_time
        }
    except Exception as e:
        logger.error(f"Erro ao atualizar índice: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/stats", response_model=ServerStatsResponse)
async def get_server_stats():
    """
    Endpoint para obter estatísticas do servidor.
    
    Returns:
        ServerStatsResponse com estatísticas de uso
    """
    uptime = time.time() - server_metrics["start_time"]
    avg_response_time = sum(server_metrics["response_times"]) / len(server_metrics["response_times"]) if server_metrics["response_times"] else 0
    
    return {
        "uptime": uptime,
        "total_requests": server_metrics["total_requests"],
        "context_requests": server_metrics["context_requests"],
        "prompt_requests": server_metrics["prompt_requests"],
        "update_requests": server_metrics["update_requests"],
        "avg_response_time": avg_response_time
    }

@app.get("/health")
async def health_check():
    """
    Endpoint para verificação de saúde do serviço.
    
    Returns:
        Dict com status de saúde
    """
    if not context_manager or not prompt_generator:
        return JSONResponse(
            status_code=503,
            content={"status": "unhealthy", "detail": "Serviços não inicializados corretamente"}
        )
    
    return {"status": "healthy", "uptime": time.time() - server_metrics["start_time"]}

def run_server(host: str = "0.0.0.0", port: int = 8000, reload: bool = False):
    """
    Inicia o servidor MCP.
    
    Args:
        host: Endereço para escutar
        port: Porta para escutar
        reload: Se deve recarregar automaticamente durante o desenvolvimento
    """
    logger.info(f"Iniciando servidor MCP em {host}:{port}")
    
    # Configurar opções de log do uvicorn
    log_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "()": "uvicorn.logging.DefaultFormatter",
                "fmt": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                "use_colors": True,
            },
        },
        "handlers": {
            "default": {
                "formatter": "default",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stderr",
            },
        },
        "loggers": {
            "uvicorn": {"handlers": ["default"], "level": "INFO"},
            "uvicorn.error": {"handlers": ["default"], "level": "INFO"},
            "uvicorn.access": {"handlers": ["default"], "level": "INFO"},
        },
    }
    
    # Adicionar log file se configurado
    if log_file:
        log_config["handlers"]["file"] = {
            "formatter": "default",
            "class": "logging.FileHandler",
            "filename": log_file,
        }
        log_config["loggers"]["uvicorn"]["handlers"].append("file")
        log_config["loggers"]["uvicorn.error"]["handlers"].append("file")
        log_config["loggers"]["uvicorn.access"]["handlers"].append("file")
    
    uvicorn.run(
        "context_guide.mcp_server.server:app", 
        host=host, 
        port=port, 
        reload=reload,
        log_config=log_config
    )

if __name__ == "__main__":
    run_server(reload=True) 