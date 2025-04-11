"""
Módulo para integração com o Cursor IDE via MCP.
Fornece funções para enviar contexto diretamente para o Cursor IDE.
"""

import logging
import json
import os
import requests
from typing import Dict, Any, Optional, Union
from pathlib import Path

# Configuração de logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

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
        
        if not self.token:
            logger.warning("Token de API do Cursor não encontrado. Configure a variável CURSOR_API_TOKEN.")
    
    def send_context_to_cursor(self, context: str, file_path: Optional[str] = None, conversation_id: Optional[str] = None) -> bool:
        """
        Envia contexto diretamente para uma conversa no Cursor IDE.
        
        Args:
            context: O contexto a ser enviado
            file_path: Caminho do arquivo em foco (opcional)
            conversation_id: ID da conversa no Cursor (opcional)
            
        Returns:
            bool: True se o envio foi bem-sucedido, False caso contrário
        """
        if not self.token:
            logger.error("Token de API do Cursor não configurado")
            return False
        
        # Preparar payload
        payload = {
            "content": context,
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
            headers = {
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json"
            }
            
            response = requests.post(url, json=payload, headers=headers)
            
            if response.status_code == 200:
                logger.info("Contexto enviado com sucesso para o Cursor IDE")
                return True
            else:
                logger.error(f"Falha ao enviar contexto: {response.status_code} - {response.text}")
                return False
                
        except Exception as e:
            logger.error(f"Erro ao enviar contexto para o Cursor: {e}")
            return False
    
    def get_context_for_query(self, query: str, num_results: int = 5) -> Dict[str, Any]:
        """
        Consulta o servidor MCP para obter contexto para uma consulta.
        
        Args:
            query: A consulta para buscar contexto
            num_results: Número de resultados a retornar
            
        Returns:
            Dict com o contexto e fontes
        """
        try:
            url = f"{self.mcp_url}/context"
            payload = {"query": query, "num_results": num_results}
            
            response = requests.post(url, json=payload)
            
            if response.status_code == 200:
                return response.json()
            else:
                logger.error(f"Falha ao obter contexto: {response.status_code} - {response.text}")
                return {"context": "", "sources": []}
                
        except Exception as e:
            logger.error(f"Erro ao consultar servidor MCP: {e}")
            return {"context": "", "sources": []}
    
    def enhance_cursor_prompt(self, user_request: str) -> bool:
        """
        Melhora o prompt do usuário no Cursor com contexto relevante.
        
        Args:
            user_request: A solicitação do usuário
            
        Returns:
            bool: True se o processo foi bem-sucedido, False caso contrário
        """
        try:
            # Obter prompt formatado com contexto
            url = f"{self.mcp_url}/prompt"
            payload = {"request": user_request}
            
            response = requests.post(url, json=payload)
            
            if response.status_code != 200:
                logger.error(f"Falha ao gerar prompt: {response.status_code} - {response.text}")
                return False
            
            # Extrair prompt formatado
            prompt_data = response.json()
            formatted_prompt = prompt_data.get("prompt", "")
            
            if not formatted_prompt:
                logger.warning("Prompt gerado está vazio")
                return False
            
            # Enviar para o Cursor
            return self.send_context_to_cursor(formatted_prompt)
                
        except Exception as e:
            logger.error(f"Erro ao melhorar prompt para o Cursor: {e}")
            return False 