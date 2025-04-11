"""
Módulo para gerar prompts com contexto para envio ao Cursor IDE.
Consulta o índice de documentos e formata prompts enriquecidos com contexto.
"""

import logging
from typing import Dict, Any, Optional, List

try:
    import pyperclip
    PYPERCLIP_AVAILABLE = True
except ImportError:
    PYPERCLIP_AVAILABLE = False
    print("Aviso: pyperclip não disponível, função de copiar para clipboard desabilitada")

try:
    from context import ContextManager
except ImportError:
    from src.context import ContextManager

# Configuração de logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class PromptGenerator:
    """Gera prompts enriquecidos com contexto para o Cursor IDE."""
    
    def __init__(self, context_manager: ContextManager):
        """
        Inicializa o gerador de prompts.
        
        Args:
            context_manager: Instância do ContextManager para consulta de contexto
        """
        self.context_manager = context_manager
    
    def generate_prompt(self, user_request: str) -> str:
        """
        Gera um prompt enriquecido com contexto relevante do projeto.
        
        Args:
            user_request: Solicitação do usuário para gerar código
            
        Returns:
            Prompt formatado com contexto para o Cursor IDE
        """
        logger.info(f"Gerando prompt para: '{user_request}'")
        
        # Obter contexto relevante
        context_data = self.context_manager.get_relevant_context(user_request)
        context_text = context_data["context"]
        
        # Extrair informações sobre fontes
        sources = []
        for source in context_data.get("sources", []):
            if source.get("metadata") and "file_path" in source["metadata"]:
                file_name = source["metadata"]["file_path"].split("/")[-1]
                sources.append(file_name)
        
        sources_text = ", ".join(set(sources)) if sources else "Nenhuma fonte específica"
        
        # Formatar o prompt
        prompt = self._format_prompt(user_request, context_text, sources_text)
        
        logger.info(f"Prompt gerado com {len(prompt)} caracteres, baseado em {sources_text}")
        return prompt
    
    def _format_prompt(self, user_request: str, context: str, sources: str) -> str:
        """
        Formata o prompt final com contexto.
        
        Args:
            user_request: Solicitação original do usuário
            context: Contexto relevante obtido do índice
            sources: Lista de fontes utilizadas no contexto
            
        Returns:
            Prompt formatado
        """
        prompt = f"""
# Solicitação: {user_request}

## Contexto do Projeto
O pedido deve ser implementado considerando o contexto atual do projeto:

{context}

## Fontes Consultadas
Este contexto foi obtido de: {sources}

## Instruções para Geração
- Mantenha consistência com os componentes e arquitetura existentes
- Não reimplemente funcionalidades já existentes
- Respeite as convenções de nomenclatura do projeto
- Forneça o código completo e funcional
- Se necessário, inclua instruções de uso

Por favor, implemente: {user_request}
"""
        return prompt.strip()
    
    def generate_and_copy_to_clipboard(self, user_request: str) -> str:
        """
        Gera um prompt e copia para a área de transferência.
        
        Args:
            user_request: Solicitação do usuário
            
        Returns:
            Prompt gerado
        """
        prompt = self.generate_prompt(user_request)
        
        if PYPERCLIP_AVAILABLE:
            try:
                pyperclip.copy(prompt)
                logger.info("Prompt copiado para a área de transferência")
            except Exception as e:
                logger.error(f"Erro ao copiar para a área de transferência: {e}")
        else:
            logger.warning("pyperclip não disponível, não foi possível copiar para área de transferência")
            print("\n" + "="*50)
            print("PROMPT GERADO (COPIE MANUALMENTE):")
            print("="*50)
            print(prompt)
            print("="*50)
        
        return prompt