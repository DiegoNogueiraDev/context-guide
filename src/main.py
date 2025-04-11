"""
Módulo principal que integra todos os componentes do MVP.
Fornece interface de linha de comando para interação com o sistema.
"""

import os
import sys
import logging
import argparse
import threading
import time
from pathlib import Path

# Corrigir importações para funcionar em qualquer contexto
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

try:
    from context import ContextManager
    from watcher import FileWatcher
    from prompt_generator import PromptGenerator
except ImportError:
    from src.context import ContextManager
    from src.watcher import FileWatcher
    from src.prompt_generator import PromptGenerator

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
        description="MVP para contextualização automática no Cursor IDE"
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
    
    # Opções globais
    parser.add_argument(
        "--docs-dir",
        default="docs",
        help="Diretório contendo os arquivos markdown (padrão: 'docs')"
    )
    parser.add_argument(
        "--db-dir",
        default="chroma_db",
        help="Diretório para o banco de dados ChromaDB (padrão: 'chroma_db')"
    )
    
    return parser.parse_args()

def main():
    """Função principal do MVP."""
    args = parse_arguments()
    
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
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()