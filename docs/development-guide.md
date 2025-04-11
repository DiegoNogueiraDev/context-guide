# Guia de Desenvolvimento - Context Guide

Este documento oferece uma visão detalhada da estrutura interna do Context Guide para desenvolvedores que desejam entender ou contribuir com o projeto.

## Visão Geral da Arquitetura

O Context Guide é construído com uma arquitetura modular em Python, projetada para facilitar extensões e personalizações:

```
context-guide/
├── context_guide/         # Código fonte principal
│   ├── __init__.py        # Inicialização do pacote
│   ├── cli.py             # Interface de linha de comando
│   ├── context.py         # Gerenciamento de contexto (RAG)
│   ├── watcher.py         # Monitoramento de alterações
│   ├── prompt_generator.py # Geração de prompts
│   └── project_templates.py # Templates de documentação
├── setup.py               # Configuração de instalação
├── pyproject.toml         # Metadados do projeto (PEP 621)
└── README.md              # Documentação principal
```

## Principais Módulos

### CLI (`cli.py`)

O módulo CLI gerencia toda a interação via linha de comando, incluindo:
- Processamento de argumentos
- Comandos disponíveis (`init`, `update`, `serve`, `generate`)
- Inicialização da estrutura do projeto
- Orquestração das diferentes funcionalidades

As principais funções são:
- `parse_arguments()`: Processa os argumentos da linha de comando
- `initialize_project()`: Cria a estrutura inicial de documentação
- `main()`: Ponto de entrada principal

### Context Manager (`context.py`)

Este módulo implementa o sistema de RAG (Retrieval Augmented Generation) usando LlamaIndex e ChromaDB:
- Indexação de documentos Markdown
- Consulta de informações relevantes
- Armazenamento e recuperação eficiente

As principais classes e métodos:
- `ContextManager`: Classe principal para gerenciar o contexto
  - `update_index()`: Atualiza o índice de documentos
  - `get_relevant_context()`: Consulta o contexto relevante para uma solicitação

### Watcher (`watcher.py`)

Responsável pelo monitoramento em tempo real de alterações nos arquivos Markdown:
- Detecção de alterações nos documentos
- Atualização automática do índice
- Gerenciamento de eventos do sistema de arquivos

A classe principal é:
- `FileWatcher`: Monitora alterações em arquivos
  - `start()`: Inicia o monitoramento
  - `stop()`: Interrompe o monitoramento

### Prompt Generator (`prompt_generator.py`)

Gera prompts enriquecidos com contexto, otimizados para IAs:
- Consulta o contexto relevante
- Formata prompts estruturados
- Copia para a área de transferência

A classe principal é:
- `PromptGenerator`: Gera prompts contextualizados
  - `generate_prompt()`: Gera um prompt para uma solicitação
  - `generate_and_copy_to_clipboard()`: Gera e copia para clipboard

### Project Templates (`project_templates.py`)

Contém templates para diferentes tipos de documentação:
- Templates básicos (visão geral, arquitetura, etc.)
- Templates de acompanhamento (tarefas, status de módulos)
- Templates de desenvolvimento (API, práticas, deployment)
- Templates específicos para tipos de aplicação (web, mobile, desktop)

## Fluxo de Dados

1. **Inicialização do Projeto**:
   ```
   CLI (initialize_project) -> Project Templates -> Sistema de Arquivos
   ```

2. **Monitoramento de Alterações**:
   ```
   FileWatcher -> Sistema de Arquivos -> Detecção de Alteração -> ContextManager (update_index)
   ```

3. **Geração de Prompts**:
   ```
   CLI (generate) -> ContextManager (get_relevant_context) -> PromptGenerator -> Clipboard
   ```

## Configuração do Ambiente de Desenvolvimento

### Requisitos

- Python 3.9+
- Pacotes listados em `requirements.txt` ou `pyproject.toml`

### Instalação para Desenvolvimento

```bash
# Clone o repositório
git clone https://github.com/seuusuario/context-guide.git
cd context-guide

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate     # Windows

# Instale em modo de desenvolvimento
pip install -e .
```

### Executando Testes

```bash
# Instalar dependências de teste
pip install pytest

# Executar testes
pytest
```

## Adicionando Novos Recursos

### Novos Comandos CLI

Para adicionar um novo comando:

1. Atualize `parse_arguments()` em `cli.py` com o novo subparser
2. Adicione a lógica de processamento no método `main()`
3. Implemente a funcionalidade em um método dedicado ou módulo

Exemplo:
```python
# Adicionando um novo comando 'export'
export_parser = subparsers.add_parser(
    "export", 
    help="Exportar documentação em outros formatos"
)
export_parser.add_argument(
    "--format",
    choices=["html", "pdf", "docx"],
    default="html",
    help="Formato de exportação"
)
```

### Novos Templates

Para adicionar novos templates:

1. Adicione a string de template em `project_templates.py`
2. Atualize o dicionário `PROJECT_TEMPLATES` para incluir o novo template
3. Modifique `initialize_project()` em `cli.py` para usar o novo template quando apropriado

### Integrações de IA Adicionais

Para integrar com novos modelos ou serviços:

1. Adicione as dependências necessárias em `setup.py` e `pyproject.toml`
2. Crie um novo módulo para gerenciar a integração
3. Atualize `prompt_generator.py` para utilizar a nova integração

## Padrões de Codificação

- Use docstrings no formato Google Python
- Mantenha a cobertura de type hints
- Siga a PEP 8 para estilo de código
- Trate exceções de forma adequada, especialmente para ferramentas externas

## Como Contribuir

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Faça commits de suas alterações (`git commit -am 'Adiciona nova feature'`)
4. Envie para o GitHub (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Modelo de Lançamento

- Versão semântica: MAJOR.MINOR.PATCH
- Branch principal: `main`
- Branches de desenvolvimento: `dev`, `feature/*`, `fix/*`

## Contato

Para questões relacionadas ao desenvolvimento, entre em contato via:
- GitHub Issues: [link para issues]
- Email: [seu.email@exemplo.com] 