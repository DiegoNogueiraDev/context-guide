"""
Context Guide - Ferramenta para fornecer contexto automático a IDEs assistidas por IA.

Este módulo fornece funcionalidades para criar, manter e consultar documentação de projeto
e utilizá-la para enriquecer prompts enviados para IDEs como o Cursor.
"""

__version__ = "0.2.0"
__author__ = "Diego Nogueira"
__email__ = "devnogueiradiego@gmail.com"

# Versões mínimas compatíveis das dependências principais
DEPENDENCIES = {
    "llama-index": "0.9.0",
    "chromadb": "0.4.18",
    "watchdog": "3.0.0"
}

# Tecnologias suportadas para contextualização especializada
SUPPORTED_TECHNOLOGIES = ["react", "node", "django", "flask", "vue", "spring"] 