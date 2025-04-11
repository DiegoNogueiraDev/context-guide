"""
Testes unitários para o Context Guide.
"""

import os
import sys
import unittest
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from context_guide import __version__
from context_guide.context import ContextManager
from context_guide.prompt_generator import PromptGenerator
from context_guide.watcher import FileWatcher

class TestContextGuide(unittest.TestCase):
    """Testes básicos para os componentes principais do Context Guide."""
    
    def test_version(self):
        """Verifica se a versão está definida."""
        self.assertIsNotNone(__version__)
    
    @patch('context_guide.context.ContextManager.get_relevant_context')
    def test_prompt_generator(self, mock_get_context):
        """Testa a geração de prompt."""
        # Configurar o mock
        mock_get_context.return_value = {
            'context': 'Contexto de teste',
            'sources': ['test.md']
        }
        
        # Criar instância com o ContextManager mockado
        context_manager = ContextManager()
        generator = PromptGenerator(context_manager)
        
        # Testar geração de prompt
        prompt = generator.generate_prompt("Teste")
        
        # Verificar se o prompt contém o contexto mockado
        self.assertIn("Contexto de teste", prompt)
        self.assertIn("test.md", prompt)
        
    def test_context_manager_init(self):
        """Testa a inicialização do ContextManager."""
        # Cria uma instância e verifica atributos básicos
        manager = ContextManager(docs_dir="test_docs", db_dir="test_db")
        
        self.assertEqual(manager.docs_dir, "test_docs")
        self.assertEqual(manager.db_dir, "test_db")
    
    @patch('time.sleep', return_value=None)
    @patch('context_guide.watcher.Observer')
    def test_file_watcher(self, mock_observer, mock_sleep):
        """Testa a inicialização e uso básico do FileWatcher."""
        # Mock para o callback
        mock_callback = MagicMock()
        
        # Criar o watcher
        watcher = FileWatcher("test_dir", mock_callback)
        
        # Testar inicialização
        self.assertEqual(watcher.directory, "test_dir")
        self.assertEqual(watcher.callback, mock_callback)
        
        # Testar métodos
        watcher.start()
        mock_observer.return_value.start.assert_called_once()
        
        watcher.stop()
        mock_observer.return_value.stop.assert_called_once()
        mock_observer.return_value.join.assert_called_once()

if __name__ == '__main__':
    unittest.main() 