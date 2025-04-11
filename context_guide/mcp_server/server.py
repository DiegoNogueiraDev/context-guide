"""
Implementação do servidor MCP (Model Control Panel) para fornecer contexto ao Cursor IDE.
Utiliza FastAPI para criar endpoints RESTful para consulta de contexto.
"""

import logging
import os
from typing import Dict, Any, Optional, List
from fastapi import FastAPI, HTTPException, Body, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

from context_guide.context import ContextManager
from context_guide.prompt_generator import PromptGenerator

# Configuração de logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Modelos de dados
class ContextRequest(BaseModel):
    """Modelo para requisições de contexto."""
    query: str
    num_results: int = 5

class PromptRequest(BaseModel):
    """Modelo para requisições de geração de prompt."""
    request: str

class ContextResponse(BaseModel):
    """Modelo para respostas com contexto."""
    context: str
    sources: List[Dict[str, Any]]

class PromptResponse(BaseModel):
    """Modelo para respostas com prompt."""
    prompt: str

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
    return {"status": "online", "service": "Context Guide MCP Server"}

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
        logger.info(f"Recebida consulta: '{request.query}'")
        result = context_manager.get_relevant_context(request.query, request.num_results)
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
        logger.info(f"Gerando prompt para: '{request.request}'")
        prompt = prompt_generator.generate_prompt(request.request)
        return {"prompt": prompt}
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
        logger.info("Atualizando índice de documentos")
        context_manager.update_index()
        return {"status": "success", "message": "Índice atualizado com sucesso"}
    except Exception as e:
        logger.error(f"Erro ao atualizar índice: {e}")
        raise HTTPException(status_code=500, detail=str(e))

def run_server(host: str = "0.0.0.0", port: int = 8000, reload: bool = False):
    """
    Inicia o servidor MCP.
    
    Args:
        host: Endereço para escutar
        port: Porta para escutar
        reload: Se deve recarregar automaticamente durante o desenvolvimento
    """
    logger.info(f"Iniciando servidor MCP em {host}:{port}")
    uvicorn.run("context_guide.mcp_server.server:app", host=host, port=port, reload=reload)

if __name__ == "__main__":
    run_server(reload=True) 