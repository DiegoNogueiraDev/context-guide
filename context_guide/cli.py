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
from context_guide.project_templates import PROJECT_TEMPLATES

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
    generate_parser.add_argument(
        "--technology",
        choices=["react", "node", "django", "flask", "vue", "spring"],
        help="Tecnologia específica para contextualização especializada"
    )
    
    # Comando para iniciar modo servidor (monitoramento)
    server_parser = subparsers.add_parser(
        "serve", 
        help="Iniciar modo servidor para monitorar alterações nos documentos"
    )
    
    # Comando para iniciar servidor MCP
    mcp_parser = subparsers.add_parser(
        "mcp",
        help="Iniciar servidor MCP para integração com Cursor IDE"
    )
    mcp_parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Host para o servidor MCP (padrão: 0.0.0.0)"
    )
    mcp_parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Porta para o servidor MCP (padrão: 8000)"
    )
    mcp_parser.add_argument(
        "--reload",
        action="store_true",
        help="Ativa o reload automático durante desenvolvimento"
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
    init_parser.add_argument(
        "--project-type",
        choices=["minimal", "standard", "complete", "web", "mobile", "desktop"],
        default="standard",
        help="Tipo de projeto a ser inicializado (padrão: standard)"
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

def initialize_project(docs_dir, project_type="standard"):
    """
    Inicializa a estrutura de documentação em um projeto existente.
    
    Args:
        docs_dir: Diretório onde os arquivos serão criados
        project_type: Tipo de estrutura de projeto a criar
    """
    docs_path = Path(docs_dir)
    docs_path.mkdir(exist_ok=True)
    
    created_files = []
    
    # Definir quais grupos de templates serão incluídos com base no tipo de projeto
    template_groups = []
    
    if project_type == "minimal":
        # Incluir apenas os templates básicos essenciais
        template_groups = ["basic"]
    elif project_type == "standard":
        # Incluir templates básicos e de acompanhamento
        template_groups = ["basic", "tracking"]
    elif project_type == "complete":
        # Incluir todos os templates
        template_groups = ["basic", "tracking", "development"]
    elif project_type == "web":
        # Incluir todos os templates mais o específico para web
        template_groups = ["basic", "tracking", "development"]
        # Adicionar o template específico para web apps
        file_path = docs_path / "architecture" / "web-app.md"
        file_path.parent.mkdir(exist_ok=True)
        if not file_path.exists():
            with open(file_path, 'w') as f:
                f.write(PROJECT_TEMPLATES["app_types"]["web-app.md"])
            created_files.append(file_path)
    elif project_type == "mobile":
        # Incluir todos os templates mais o específico para mobile
        template_groups = ["basic", "tracking", "development"]
        # Adicionar o template específico para mobile apps
        file_path = docs_path / "architecture" / "mobile-app.md"
        file_path.parent.mkdir(exist_ok=True)
        if not file_path.exists():
            with open(file_path, 'w') as f:
                f.write(PROJECT_TEMPLATES["app_types"]["mobile-app.md"])
            created_files.append(file_path)
    elif project_type == "desktop":
        # Incluir todos os templates mais o específico para desktop
        template_groups = ["basic", "tracking", "development"]
        # Adicionar o template específico para desktop apps
        file_path = docs_path / "architecture" / "desktop-app.md"
        file_path.parent.mkdir(exist_ok=True)
        if not file_path.exists():
            with open(file_path, 'w') as f:
                f.write(PROJECT_TEMPLATES["app_types"]["desktop-app.md"])
            created_files.append(file_path)
    
    # Criar os arquivos de acordo com os grupos selecionados
    for group in template_groups:
        if group in PROJECT_TEMPLATES:
            for filename, content in PROJECT_TEMPLATES[group].items():
                # Para melhor organização, colocar templates de desenvolvimento em subpasta
                if group == "development":
                    file_path = docs_path / "development" / filename
                    file_path.parent.mkdir(exist_ok=True)
                elif group == "tracking":
                    file_path = docs_path / "tracking" / filename
                    file_path.parent.mkdir(exist_ok=True)
                else:
                    file_path = docs_path / filename
                
                if not file_path.exists():
                    with open(file_path, 'w') as f:
                        f.write(content)
                    created_files.append(file_path)
    
    # Resumo dos arquivos criados
    print(f"\n🎉 Inicialização concluída! Criados {len(created_files)} arquivos de documentação.")
    
    # Mostrar os arquivos criados agrupados por categoria
    if created_files:
        print("\nArquivos criados:")
        
        categories = {
            "basic": "Documentação Básica",
            "tracking": "Acompanhamento de Desenvolvimento",
            "development": "Guias de Desenvolvimento",
            "app_types": "Arquitetura Específica"
        }
        
        for category, label in categories.items():
            category_files = [f for f in created_files if category in str(f)]
            if category_files:
                print(f"\n📁 {label}:")
                for file in category_files:
                    print(f"  ✅ {file}")
    
    # Adicionar .context_guide ao .gitignore se existir
    gitignore_path = Path('.gitignore')
    if gitignore_path.exists():
        with open(gitignore_path, 'r') as f:
            content = f.read()
        
        if '.context_guide' not in content:
            with open(gitignore_path, 'a') as f:
                f.write("\n# Context Guide\n.context_guide/\n")
            print("\n✅ Adicionado .context_guide ao .gitignore")
    
    print("\n🚀 Próximos passos:")
    print("1. Atualize os arquivos markdown com informações do seu projeto")
    print("2. Execute 'context-guide update' para indexar os documentos")
    print("3. Use 'context-guide generate \"Sua solicitação\"' para gerar prompts com contexto")
    print("\n📚 Documentação completa disponível em: https://github.com/seuusuario/context-guide")

def main():
    """Função principal do Context Guide."""
    args = parse_arguments()
    
    # Comando de inicialização
    if args.command == "init":
        project_type = getattr(args, "project_type", "standard")
        initialize_project(args.docs_dir, project_type)
        return
    
    # Comando para iniciar servidor MCP
    if args.command == "mcp":
        print(f"🚀 Iniciando servidor MCP em {args.host}:{args.port}...")
        
        try:
            # Importar sob demanda para evitar dependências desnecessárias
            from context_guide.mcp_server.server import run_server
            
            # Definir variáveis de ambiente para configuração
            os.environ["CONTEXT_GUIDE_DOCS_DIR"] = args.docs_dir
            os.environ["CONTEXT_GUIDE_DB_DIR"] = args.db_dir
            
            # Iniciar o servidor MCP
            run_server(host=args.host, port=args.port, reload=args.reload)
        except ImportError:
            print("\n❌ Erro: Dependências para o servidor MCP não encontradas.")
            print("Por favor, instale as dependências necessárias:")
            print("pip install fastapi uvicorn requests pydantic")
            sys.exit(1)
        except Exception as e:
            logger.error(f"Erro ao iniciar servidor MCP: {e}")
            sys.exit(1)
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
            # Verificar se há tecnologia especificada
            technology = getattr(args, "technology", None)
            if technology:
                print(f"⚙️ Usando contextualização especializada para: {technology}")
                # Adicionar contexto de tecnologia à solicitação
                request_with_tech = f"{request} (technology: {technology})"
            else:
                request_with_tech = request
            
            # Gerar prompt e copiar para área de transferência
            prompt = prompt_generator.generate_and_copy_to_clipboard(request_with_tech)
            
            # Exibir resumo do prompt
            print("\n" + "="*50)
            print("✅ Prompt gerado e copiado para área de transferência!")
            print("="*50)
            print(f"Solicitação: {request}")
            if technology:
                print(f"Tecnologia: {technology}")
            
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
            print("\n🔄 Monitorando alterações em documentos markdown...")
            print("⌨️  Pressione Ctrl+C para encerrar")
            
            # Manter o programa rodando
            while True:
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("\n🛑 Interrompido pelo usuário")
        except Exception as e:
            logger.error(f"Erro no servidor: {e}")
        finally:
            # Garantir que o observador seja encerrado
            if file_watcher:
                file_watcher.stop()
            print("👋 Servidor encerrado")
    
    elif args.command == "update":
        print(f"📚 Atualizando índice para documentos em '{args.docs_dir}'...")
        
        try:
            context_manager.update_index()
            print("✅ Índice atualizado com sucesso!")
        except Exception as e:
            logger.error(f"Erro ao atualizar índice: {e}")
            sys.exit(1)
    
    else:
        print("Nenhum comando especificado. Use --help para ver as opções disponíveis.")
        
if __name__ == "__main__":
    main() 