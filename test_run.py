#!/usr/bin/env python3
"""
Script para testar execução do MVP Context Cursor.
"""

import os
import sys

# Adicionar diretório atual ao path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Tentar importar e executar o código
try:
    from src.main import main
    print("Módulo importado com sucesso!")
    print("Teste concluído com sucesso!")
except Exception as e:
    print(f"Erro ao importar módulo: {e}")

if __name__ == "__main__":
    print("Iniciando teste de importação...")
    print(f"Python path: {sys.path}")
    print(f"Diretório atual: {os.getcwd()}") 