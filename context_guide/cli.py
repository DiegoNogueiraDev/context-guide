#!/usr/bin/env python3
"""
Command Line Interface para o Context Guide.
Fornece comandos para gerar prompts, monitorar documentos e atualizar índices.
"""

import os
import sys
import logging
import argparse
import threading
import time
from pathlib import Path

from context_guide.context import ContextManager
from context_guide.watcher import FileWatcher
from context_guide.prompt_generator import PromptGenerator

# Configuração de logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def parse_arguments():
    """
    Processa argumentos da linha de comando.
    
    Returns:
        Argumentos processados
    """
    parser = argparse.ArgumentParser(
        description="Context Guide - Contextualização automática para IDEs assistidas por IA"
    )
    
    # Comandos principais
    subparsers = parser.add_subparsers(dest="command", help="Comando a executar")
    
    # Comando para gerar prompt
    generate_parser = subparsers.add_parser("generate", help="Gerar prompt com contexto")
    generate_parser.add_argument(
        "request",
        nargs="+",
        help="Solicitação para gerar código (ex: 'Criar componente ProfileCard')"
    )
    
    # Comando para iniciar modo servidor (monitoramento)
    server_parser = subparsers.add_parser(
        "serve", 
        help="Iniciar modo servidor para monitorar alterações nos documentos"
    )
    
    # Comando para atualizar índice
    update_parser = subparsers.add_parser(
        "update", 
        help="Atualizar manualmente o índice de documentos"
    )
    
    # Comando para inicializar estrutura em um projeto
    init_parser = subparsers.add_parser(
        "init",
        help="Inicializar estrutura de documentação em um projeto existente"
    )
    
    # Opções globais
    parser.add_argument(
        "--docs-dir",
        default="docs",
        help="Diretório contendo os arquivos markdown (padrão: 'docs')"
    )
    parser.add_argument(
        "--db-dir",
        default=".context_guide",
        help="Diretório para o banco de dados ChromaDB (padrão: '.context_guide')"
    )
    
    return parser.parse_args()

def initialize_project(docs_dir):
    """
    Inicializa a estrutura de documentação em um projeto existente.
    
    Args:
        docs_dir: Diretório onde os arquivos serão criados
    """
    docs_path = Path(docs_dir)
    docs_path.mkdir(exist_ok=True)
    
    # Criar arquivos de exemplo se não existirem
    overview_path = docs_path / "overview.md"
    if not overview_path.exists():
        with open(overview_path, 'w') as f:
            f.write("""# Visão Geral do Projeto

Descreva aqui o propósito geral e tecnologias do seu projeto.

## Propósito
Explique o objetivo principal do projeto.

## Tecnologias Principais
- Framework principal
- Linguagem
- Outras tecnologias importantes
""")
        print(f"✅ Criado arquivo {overview_path}")
    
    components_path = docs_path / "components.md"
    if not components_path.exists():
        with open(components_path, 'w') as f:
            f.write("""# Componentes do Projeto

Liste aqui os principais componentes do seu projeto e suas propriedades.

## Componentes de UI
- **ComponenteA** (`prop1: tipo, prop2: tipo`) - Descrição do componente
- **ComponenteB** (`prop1: tipo, prop2: tipo`) - Descrição do componente

## Outros Componentes
- **ComponenteC** (`prop1: tipo, prop2: tipo`) - Descrição do componente
""")
        print(f"✅ Criado arquivo {components_path}")
    
    features_path = docs_path / "features.md"
    if not features_path.exists():
        with open(features_path, 'w') as f:
            f.write("""# Funcionalidades do Projeto

Liste aqui as principais funcionalidades do seu projeto.

## Funcionalidade A
- Descrição da funcionalidade
- Sub-funcionalidades relacionadas

## Funcionalidade B
- Descrição da funcionalidade
- Sub-funcionalidades relacionadas
""")
        print(f"✅ Criado arquivo {features_path}")
    
    architecture_path = docs_path / "architecture.md"
    if not architecture_path.exists():
        with open(architecture_path, 'w') as f:
            f.write("""# Arquitetura do Projeto

Descreva aqui a arquitetura do seu projeto.

## Frontend
- **Framework**: 
- **Gerenciamento de Estado**: 
- **Estilização**: 

## Backend
- **API**: 
- **Banco de Dados**: 
- **Autenticação**: 

## Infraestrutura
- **Deploy**: 
- **CI/CD**: 
""")
        print(f"✅ Criado arquivo {architecture_path}")
    
    # Adicionar .context_guide ao .gitignore se existir
    gitignore_path = Path('.gitignore')
    if gitignore_path.exists():
        with open(gitignore_path, 'r') as f:
            content = f.read()
        
        if '.context_guide' not in content:
            with open(gitignore_path, 'a') as f:
                f.write("\n# Context Guide\n.context_guide/\n")
            print("✅ Adicionado .context_guide ao .gitignore")
    
    print("\n🎉 Inicialização concluída!")
    print(f"Edite os arquivos em '{docs_dir}/' para refletir os detalhes do seu projeto.")
    print("\nPróximos passos:")
    print("1. Atualize os arquivos markdown com informações do seu projeto")
    print("2. Execute 'context-guide update' para indexar os documentos")
    print("3. Use 'context-guide generate \"Sua solicitação\"' para gerar prompts com contexto")

def main():
    """Função principal do Context Guide."""
    args = parse_arguments()
    
    # Comando de inicialização
    if args.command == "init":
        initialize_project(args.docs_dir)
        return
    
    # Criar instância do gerenciador de contexto
    try:
        context_manager = ContextManager(docs_dir=args.docs_dir, db_dir=args.db_dir)
        prompt_generator = PromptGenerator(context_manager)
    except Exception as e:
        logger.error(f"Erro ao inicializar sistema: {e}")
        sys.exit(1)
    
    # Processar comando
    if args.command == "generate":
        # Juntar as palavras da solicitação
        request = " ".join(args.request)
        
        try:
            # Gerar prompt e copiar para área de transferência
            prompt = prompt_generator.generate_and_copy_to_clipboard(request)
            
            # Exibir resumo do prompt
            print("\n" + "="*50)
            print("✅ Prompt gerado e copiado para área de transferência!")
            print("="*50)
            print(f"Solicitação: {request}")
            
            # Oferecer opção para mostrar o prompt completo
            show_full = input("\nMostrar prompt completo? (s/N): ").lower() == 's'
            if show_full:
                print("\n" + "="*50)
                print("PROMPT COMPLETO:")
                print("="*50)
                print(prompt)
                print("="*50)
            
            print("\n💡 Cole este prompt diretamente no Cursor IDE para gerar código com contexto.")
            
        except Exception as e:
            logger.error(f"Erro ao gerar prompt: {e}")
            sys.exit(1)
    
    elif args.command == "serve":
        print(f"🔍 Iniciando servidor de monitoramento para '{args.docs_dir}'...")
        
        # Criar e iniciar observador de arquivos
        def update_callback():
            print(f"\n📝 Detectada alteração em documentos. Atualizando índice...")
            context_manager.update_index()
            print(f"✅ Índice atualizado em {time.strftime('%H:%M:%S')}")
        
        file_watcher = FileWatcher(args.docs_dir, update_callback)
        
        try:
            file_watcher.start()
            print("✅ Servidor iniciado com sucesso!")
            print("📋 Use outro terminal para executar comandos 'generate' enquanto o servidor está rodando.")
            print("🛑 Pressione Ctrl+C para interromper...")
            
            # Manter a thread principal viva
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n🛑 Encerrando servidor...")
            file_watcher.stop()
            print("✅ Servidor encerrado.")
        except Exception as e:
            logger.error(f"Erro no servidor: {e}")
            file_watcher.stop()
            sys.exit(1)
    
    elif args.command == "update":
        print("🔄 Atualizando índice de documentos...")
        try:
            context_manager.update_index()
            print("✅ Índice atualizado com sucesso!")
        except Exception as e:
            logger.error(f"Erro ao atualizar índice: {e}")
            sys.exit(1)
    
    else:
        # Se nenhum comando foi especificado, mostrar a ajuda
        print("Por favor, especifique um comando. Use --help para obter ajuda.")
        parser = argparse.ArgumentParser()
        subparsers = parser.add_subparsers()
        subparsers.add_parser("generate")
        subparsers.add_parser("serve")
        subparsers.add_parser("update")
        subparsers.add_parser("init")
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main() 