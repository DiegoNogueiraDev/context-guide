"""
Módulo para integração com o Cursor IDE via MCP.
Fornece funções para enviar contexto diretamente para o Cursor IDE.
"""

import logging
import json
import os
import time
from typing import Dict, Any, Optional, Union, List
from pathlib import Path
import requests

# Configuração de logging
log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
log_level = os.environ.get('CONTEXT_GUIDE_LOG_LEVEL', 'INFO')
log_file = os.environ.get('CONTEXT_GUIDE_LOG_FILE', None)

handlers = [logging.StreamHandler()]
if log_file:
    handlers.append(logging.FileHandler(log_file))

logging.basicConfig(level=getattr(logging, log_level), format=log_format, handlers=handlers)
logger = logging.getLogger(__name__)

# Tecnologias suportadas e seus contextos especiais
TECH_CONTEXTS = {
    "react": {
        "description": "Biblioteca JavaScript para construção de interfaces de usuário",
        "common_patterns": ["componentes funcionais", "hooks", "props", "estado", "contexto"],
        "best_practices": [
            "Utilizar componentes funcionais com hooks",
            "Evitar renderizações desnecessárias",
            "Separar lógica de UI da lógica de negócios",
            "Utilizar gerenciamento de estado apropriado para o tamanho da aplicação"
        ]
    },
    "node": {
        "description": "Ambiente de execução JavaScript do lado do servidor",
        "common_patterns": ["middleware", "rotas", "controladores", "modelos", "serviços"],
        "best_practices": [
            "Organizar o código em camadas (controllers, services, models)",
            "Usar async/await para operações assíncronas",
            "Implementar tratamento de erros centralizado",
            "Validar entradas e sanitizar saídas"
        ]
    },
    "django": {
        "description": "Framework web Python de alto nível",
        "common_patterns": ["views", "models", "templates", "forms", "admin"],
        "best_practices": [
            "Seguir o padrão MVT (Model-View-Template)",
            "Utilizar ORM para abstração do banco de dados",
            "Manter views pequenas e focadas",
            "Usar Django REST Framework para APIs"
        ]
    },
    "flask": {
        "description": "Microframework web Python",
        "common_patterns": ["rotas", "blueprints", "extensões", "contexto"],
        "best_practices": [
            "Estruturar aplicação com blueprints para escalabilidade",
            "Usar extensões para funcionalidades comuns",
            "Centralizar configuração",
            "Implementar padrão de fábrica de aplicação"
        ]
    },
    "vue": {
        "description": "Framework JavaScript progressivo para UIs",
        "common_patterns": ["componentes", "diretivas", "props", "emits", "composition API"],
        "best_practices": [
            "Utilizar Single-File Components",
            "Preferir Composition API para componentes complexos",
            "Organizar código por funcionalidade em vez de tipo",
            "Utilizar Pinia para gerenciamento de estado"
        ]
    },
    "spring": {
        "description": "Framework Java para desenvolvimento de aplicações",
        "common_patterns": ["controladores", "serviços", "repositórios", "entidades", "DTOs"],
        "best_practices": [
            "Seguir arquitetura em camadas",
            "Usar injeção de dependências",
            "Implementar testes de unidade e integração",
            "Utilizar Spring Data para acesso a dados"
        ]
    }
}

class CursorIntegration:
    """Classe para interagir com o Cursor IDE via MCP."""
    
    def __init__(self, mcp_url: str = "http://localhost:8000"):
        """
        Inicializa a integração com o Cursor.
        
        Args:
            mcp_url: URL base para o servidor MCP
        """
        self.mcp_url = mcp_url
        self.token = os.environ.get("CURSOR_API_TOKEN", "")
        self.api_base = "https://api.cursor.sh/v1"
        self.session = requests.Session()
        
        # Configurar cabeçalhos padrão
        if self.token:
            self.session.headers.update({
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json"
            })
        
        if not self.token:
            logger.warning(
                "Token de API do Cursor não encontrado. Configure a variável CURSOR_API_TOKEN. "
                "Visite https://cursor.sh/docs/api-tokens para obter seu token."
            )
    
    def send_context_to_cursor(self, 
                              context: str, 
                              file_path: Optional[str] = None, 
                              conversation_id: Optional[str] = None,
                              technology: Optional[str] = None) -> bool:
        """
        Envia contexto diretamente para uma conversa no Cursor IDE.
        
        Args:
            context: O contexto a ser enviado
            file_path: Caminho do arquivo em foco (opcional)
            conversation_id: ID da conversa no Cursor (opcional)
            technology: Tecnologia específica para enriquecer o contexto (opcional)
            
        Returns:
            bool: True se o envio foi bem-sucedido, False caso contrário
        """
        if not self.token:
            logger.error("Token de API do Cursor não configurado")
            return False
        
        # Enriquecer contexto com informações específicas da tecnologia
        enhanced_context = context
        if technology and technology.lower() in TECH_CONTEXTS:
            tech_info = TECH_CONTEXTS[technology.lower()]
            tech_context = f"\n\n## Contexto Específico: {technology}\n"
            tech_context += f"- {tech_info['description']}\n"
            tech_context += "- Padrões comuns: " + ", ".join(tech_info['common_patterns']) + "\n"
            tech_context += "- Melhores práticas:\n"
            for practice in tech_info['best_practices']:
                tech_context += f"  - {practice}\n"
            
            enhanced_context = context + tech_context
            logger.info(f"Contexto enriquecido com informações específicas de {technology}")
        
        # Preparar payload
        payload = {
            "content": enhanced_context,
            "role": "system"
        }
        
        # Adicionar file_path se fornecido
        if file_path:
            payload["file_path"] = str(Path(file_path).absolute())
        
        # Adicionar conversation_id se fornecido
        url = f"{self.api_base}/chat/message"
        if conversation_id:
            url = f"{url}?conversation_id={conversation_id}"
        
        try:
            start_time = time.time()
            response = self.session.post(url, json=payload)
            
            if response.status_code == 200:
                logger.info(f"Contexto enviado com sucesso para o Cursor IDE em {time.time() - start_time:.4f}s")
                return True
            else:
                logger.error(f"Falha ao enviar contexto: {response.status_code} - {response.text}")
                return False
                
        except Exception as e:
            logger.error(f"Erro ao enviar contexto para o Cursor: {e}")
            return False
    
    def get_context_for_query(self, 
                             query: str, 
                             num_results: int = 5,
                             technology: Optional[str] = None) -> Dict[str, Any]:
        """
        Consulta o servidor MCP para obter contexto para uma consulta.
        
        Args:
            query: A consulta para buscar contexto
            num_results: Número de resultados a retornar
            technology: Tecnologia específica para aprimorar a busca de contexto
            
        Returns:
            Dict com o contexto e fontes
        """
        try:
            url = f"{self.mcp_url}/context"
            payload = {
                "query": query, 
                "num_results": num_results
            }
            
            if technology:
                payload["technology_context"] = technology
                logger.info(f"Consultando contexto para '{query}' com tecnologia '{technology}'")
            else:
                logger.info(f"Consultando contexto para '{query}'")
            
            start_time = time.time()
            response = self.session.post(url, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                logger.info(f"Contexto obtido em {time.time() - start_time:.4f}s com {len(result.get('sources', []))} fontes")
                return result
            else:
                logger.error(f"Falha ao obter contexto: {response.status_code} - {response.text}")
                return {"context": "", "sources": []}
                
        except Exception as e:
            logger.error(f"Erro ao consultar servidor MCP: {e}")
            return {"context": "", "sources": []}
    
    def enhance_cursor_prompt(self, 
                             user_request: str, 
                             technology: Optional[str] = None,
                             include_best_practices: bool = True) -> bool:
        """
        Melhora o prompt do usuário no Cursor com contexto relevante.
        
        Args:
            user_request: A solicitação do usuário
            technology: Tecnologia específica para ajustar o contexto
            include_best_practices: Se deve incluir melhores práticas no prompt
            
        Returns:
            bool: True se o processo foi bem-sucedido, False caso contrário
        """
        try:
            # Obter prompt formatado com contexto
            url = f"{self.mcp_url}/prompt"
            payload = {
                "request": user_request,
                "include_best_practices": include_best_practices
            }
            
            if technology:
                payload["technology_context"] = technology
                logger.info(f"Gerando prompt para '{user_request}' com tecnologia '{technology}'")
            else:
                logger.info(f"Gerando prompt para '{user_request}'")
            
            start_time = time.time()
            response = self.session.post(url, json=payload)
            
            if response.status_code != 200:
                logger.error(f"Falha ao gerar prompt: {response.status_code} - {response.text}")
                return False
            
            # Extrair prompt formatado
            prompt_data = response.json()
            formatted_prompt = prompt_data.get("prompt", "")
            generation_time = prompt_data.get("generation_time", 0)
            
            if not formatted_prompt:
                logger.warning("Prompt gerado está vazio")
                return False
            
            logger.info(f"Prompt gerado em {generation_time}s, enviando para o Cursor IDE")
            
            # Enviar para o Cursor
            return self.send_context_to_cursor(formatted_prompt, technology=technology)
                
        except Exception as e:
            logger.error(f"Erro ao melhorar prompt para o Cursor: {e}")
            return False
    
    def update_index(self) -> bool:
        """
        Solicita atualização do índice de documentos no servidor MCP.
        
        Returns:
            bool: True se a atualização foi bem-sucedida, False caso contrário
        """
        try:
            url = f"{self.mcp_url}/update-index"
            
            logger.info("Solicitando atualização do índice")
            start_time = time.time()
            response = self.session.post(url)
            
            if response.status_code == 200:
                result = response.json()
                update_time = result.get("update_time", 0)
                logger.info(f"Índice atualizado com sucesso em {update_time:.2f}s")
                return True
            else:
                logger.error(f"Falha ao atualizar índice: {response.status_code} - {response.text}")
                return False
                
        except Exception as e:
            logger.error(f"Erro ao solicitar atualização do índice: {e}")
            return False
    
    def get_server_stats(self) -> Dict[str, Any]:
        """
        Obtém estatísticas do servidor MCP.
        
        Returns:
            Dict com estatísticas do servidor
        """
        try:
            url = f"{self.mcp_url}/stats"
            
            logger.info("Consultando estatísticas do servidor")
            response = self.session.get(url)
            
            if response.status_code == 200:
                stats = response.json()
                logger.info(f"Estatísticas obtidas: {stats['total_requests']} requisições, "
                           f"uptime {stats['uptime']:.2f}s, tempo médio {stats['avg_response_time']:.4f}s")
                return stats
            else:
                logger.error(f"Falha ao obter estatísticas: {response.status_code} - {response.text}")
                return {}
                
        except Exception as e:
            logger.error(f"Erro ao consultar estatísticas do servidor: {e}")
            return {}
    
    def check_server_health(self) -> bool:
        """
        Verifica se o servidor MCP está funcionando corretamente.
        
        Returns:
            bool: True se o servidor está saudável, False caso contrário
        """
        try:
            url = f"{self.mcp_url}/health"
            
            response = self.session.get(url)
            
            if response.status_code == 200:
                health_data = response.json()
                if health_data.get("status") == "healthy":
                    uptime = health_data.get("uptime", 0)
                    logger.info(f"Servidor MCP está saudável, uptime: {uptime:.2f}s")
                    return True
            
            logger.warning(f"Servidor MCP não está saudável: {response.status_code} - {response.text}")
            return False
                
        except Exception as e:
            logger.error(f"Erro ao verificar saúde do servidor MCP: {e}")
            return False 