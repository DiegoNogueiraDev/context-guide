"""
Testes para o servidor MCP e integração com Cursor IDE.
"""

import os
import unittest
from unittest.mock import patch, MagicMock
import json
from fastapi.testclient import TestClient

# Importações condicionais para permitir testes mesmo sem as dependências opcionais
try:
    from context_guide.mcp_server.server import app
    from context_guide.mcp_server.cursor_integration import CursorIntegration
    FASTAPI_AVAILABLE = True
except ImportError:
    FASTAPI_AVAILABLE = False
    
# Skippa todos os testes se as dependências não estiverem disponíveis
@unittest.skipIf(not FASTAPI_AVAILABLE, "Dependências do MCP não estão instaladas")
class TestMCPServer(unittest.TestCase):
    """Testes para o servidor MCP."""
    
    def setUp(self):
        """Configurar ambiente de teste."""
        if FASTAPI_AVAILABLE:
            self.client = TestClient(app)
            
            # Mock para o ContextManager e PromptGenerator
            self.context_manager_patcher = patch('context_guide.mcp_server.server.context_manager')
            self.prompt_generator_patcher = patch('context_guide.mcp_server.server.prompt_generator')
            
            self.mock_context_manager = self.context_manager_patcher.start()
            self.mock_prompt_generator = self.prompt_generator_patcher.start()
            
            # Configurar valores de retorno para os mocks
            mock_context_result = {
                "context": "Contexto de teste para a consulta",
                "sources": [{"content": "Conteúdo de teste", "metadata": {"file_path": "docs/test.md"}}]
            }
            
            app.state.context_manager = self.mock_context_manager
            app.state.prompt_generator = self.mock_prompt_generator
            
            # Configurar retornos para os mocks
            self.mock_context_manager.get_relevant_context.return_value = mock_context_result
            self.mock_prompt_generator.generate_prompt.return_value = "Prompt de teste gerado"
    
    def tearDown(self):
        """Limpar ambiente após testes."""
        if FASTAPI_AVAILABLE:
            self.context_manager_patcher.stop()
            self.prompt_generator_patcher.stop()
    
    def test_root_endpoint(self):
        """Testar o endpoint raiz."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "online")
        self.assertEqual(data["service"], "Context Guide MCP Server")
    
    def test_context_endpoint(self):
        """Testar o endpoint de contexto."""
        payload = {"query": "Como implementar autenticação?", "num_results": 3}
        response = self.client.post("/context", json=payload)
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("context", data)
        self.assertIn("sources", data)
        
        # Verificar se o método correto foi chamado
        self.mock_context_manager.get_relevant_context.assert_called_once_with(
            "Como implementar autenticação?", 3
        )
    
    def test_prompt_endpoint(self):
        """Testar o endpoint de geração de prompt."""
        payload = {"request": "Criar componente de login"}
        response = self.client.post("/prompt", json=payload)
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("prompt", data)
        self.assertEqual(data["prompt"], "Prompt de teste gerado")
        
        # Verificar se o método correto foi chamado
        self.mock_prompt_generator.generate_prompt.assert_called_once_with(
            "Criar componente de login"
        )

@unittest.skipIf(not FASTAPI_AVAILABLE, "Dependências do MCP não estão instaladas")
class TestCursorIntegration(unittest.TestCase):
    """Testes para a integração com o Cursor IDE."""
    
    def setUp(self):
        """Configurar ambiente de teste."""
        # Mock para requests
        self.requests_patcher = patch('context_guide.mcp_server.cursor_integration.requests')
        self.mock_requests = self.requests_patcher.start()
        
        # Configurar mock para os.environ para o token
        self.env_patcher = patch.dict('os.environ', {"CURSOR_API_TOKEN": "test-token-123"})
        self.env_patcher.start()
        
        # Instanciar a classe de integração
        self.cursor_integration = CursorIntegration(mcp_url="http://testserver:8000")
        
        # Configurar resposta de mock para requests
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "context": "Contexto de teste",
            "sources": [{"content": "Conteúdo de teste", "metadata": {"file_path": "docs/test.md"}}],
            "prompt": "Prompt de teste"
        }
        self.mock_requests.post.return_value = mock_response
    
    def tearDown(self):
        """Limpar ambiente após testes."""
        self.requests_patcher.stop()
        self.env_patcher.stop()
    
    def test_send_context_to_cursor(self):
        """Testar envio de contexto para o Cursor IDE."""
        result = self.cursor_integration.send_context_to_cursor("Contexto de teste")
        
        self.assertTrue(result)
        self.mock_requests.post.assert_called_once()
        
        # Verificar se a URL e headers estão corretos
        args, kwargs = self.mock_requests.post.call_args
        self.assertEqual(args[0], "https://api.cursor.sh/v1/chat/message")
        self.assertEqual(kwargs["headers"]["Authorization"], "Bearer test-token-123")
    
    def test_get_context_for_query(self):
        """Testar obtenção de contexto do servidor MCP."""
        context = self.cursor_integration.get_context_for_query("Como implementar autenticação?")
        
        self.assertEqual(context["context"], "Contexto de teste")
        self.assertEqual(len(context["sources"]), 1)
        
        # Verificar se a URL e payload estão corretos
        args, kwargs = self.mock_requests.post.call_args
        self.assertEqual(args[0], "http://testserver:8000/context")
        self.assertEqual(kwargs["json"]["query"], "Como implementar autenticação?")
    
    def test_enhance_cursor_prompt(self):
        """Testar melhoria de prompt para o Cursor."""
        result = self.cursor_integration.enhance_cursor_prompt("Criar componente de login")
        
        self.assertTrue(result)
        # Verificar se foram feitas duas chamadas (uma para /prompt e outra para o Cursor)
        self.assertEqual(self.mock_requests.post.call_count, 2)

if __name__ == "__main__":
    unittest.main() 