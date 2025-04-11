# Context Guide

**Context Guide** é uma ferramenta poderosa para fornecer contexto automático ao Cursor IDE e outras IDEs assistidas por IA, ajudando a evitar perda de contexto e alucinações em projetos de qualquer linguagem.

## ⭐ Recursos Principais

- **Markdown como fonte única de contexto**: Documentação em arquivos simples
- **RAG via LlamaIndex e ChromaDB**: Indexação e busca eficiente por embeddings
- **Compatível com qualquer projeto/linguagem**: Funciona independentemente da linguagem do projeto
- **Atualização automática em tempo real**: Detecta alterações nos arquivos Markdown e atualiza o índice
- **Geração de prompts enriquecidos**: Consulta automática do contexto relevante antes de gerar código
- **Fácil integração**: Copia o prompt para a área de transferência para uso no Cursor IDE
- **Templates completos de documentação**: Guias e modelos para todos os aspectos do desenvolvimento
- **Acompanhamento do progresso**: Monitoramento de tarefas, módulos e testes
- **Arquiteturas recomendadas**: Templates para Web, Mobile e Desktop

## 🛠️ Instalação

### Opção 1: Instalação via pip (recomendado)

```bash
pip install context-guide
```

### Opção 2: Instalação a partir do código-fonte

```bash
git clone https://github.com/seuusuario/context-guide.git
cd context-guide
pip install -e .
```

## 🚀 Uso Rápido

### 1. Inicializar um novo projeto

```bash
# Navegue até a pasta do seu projeto
cd meu-projeto

# Para um projeto padrão
context-guide init

# Para uma estrutura completa com todos os templates
context-guide init --project-type complete

# Para um projeto específico
context-guide init --project-type web  # ou mobile, desktop
```

### 2. Atualize os arquivos Markdown com informações do seu projeto

Edite os arquivos criados na pasta `docs/`:
- Documentação Básica (ex: `overview.md`, `architecture.md`)
- Documentos de Acompanhamento (ex: `tracking/tasks.md`, `tracking/modules-status.md`)
- Guias de Desenvolvimento (ex: `development/api-docs.md`, `development/deployment.md`)
- Arquiteturas Específicas (ex: `architecture/web-app.md`)

### 3. Atualize o índice de contexto

```bash
context-guide update
```

### 4. Inicie o servidor de monitoramento (opcional)

Em um terminal dedicado, execute:

```bash
context-guide serve
```

### 5. Gere prompts com contexto

```bash
context-guide generate "Criar componente ProfileCard com foto e biografia"
```

### 6. Cole o prompt no Cursor IDE

O prompt gerado é automaticamente copiado para sua área de transferência. Cole-o diretamente no Cursor IDE para obter código que respeita o contexto do seu projeto.

## 📚 Estrutura e Tipos de Projetos

O Context Guide oferece diferentes modelos de documentação para diversos tipos de projetos:

### Modelos Disponíveis

- **minimal**: Apenas documentos básicos do projeto
- **standard** (padrão): Documentos básicos + acompanhamento de progresso
- **complete**: Todos os documentos (básicos, acompanhamento, desenvolvimento)
- **web**: Modelo completo + template específico para aplicações web
- **mobile**: Modelo completo + template específico para aplicações mobile
- **desktop**: Modelo completo + template específico para aplicações desktop

### Estrutura de Documentação

```
docs/
├── overview.md               # Visão geral do projeto
├── architecture.md           # Arquitetura geral
├── components.md             # Componentes do sistema
├── features.md               # Funcionalidades
│
├── tracking/                 # Acompanhamento de desenvolvimento
│   ├── tasks.md              # Tarefas e progresso
│   ├── modules-status.md     # Status dos módulos
│   └── testing-status.md     # Status dos testes
│
├── development/              # Guias de desenvolvimento
│   ├── api-docs.md           # Documentação da API
│   ├── best-practices.md     # Melhores práticas
│   ├── tools-environment.md  # Ferramentas e ambiente
│   └── deployment.md         # Guia de deployment
│
└── architecture/             # Arquiteturas específicas (opcional)
    ├── web-app.md            # Para aplicações web
    ├── mobile-app.md         # Para aplicações mobile
    └── desktop-app.md        # Para aplicações desktop
```

## 📋 Usando os Templates de Acompanhamento

### Acompanhamento de Tarefas

O arquivo `tracking/tasks.md` foi projetado para manter um registro organizado das tarefas do projeto:

- **Visão Geral do Progresso**: Acompanhe o progresso total
- **Tarefas Atuais**: Visualize o que está em desenvolvimento agora
- **Tarefas Concluídas**: Histórico do que foi realizado
- **Bloqueios e Impedimentos**: Identificação e resolução de obstáculos

### Monitoramento de Módulos

Use `tracking/modules-status.md` para acompanhar o estado de cada componente:

- **Visão Geral**: Estatísticas rápidas sobre os módulos
- **Status por Módulo**: Detalhes por componente (Frontend, Backend, etc.)
- **Dependências Externas**: Monitoramento de bibliotecas e serviços

### Status de Testes

O arquivo `tracking/testing-status.md` permite acompanhar a qualidade do código:

- **Sumário de Testes**: Cobertura e resultados gerais
- **Status por Grupo**: Detalhes por tipo de teste (unitários, integração, etc.)
- **Falhas Recorrentes**: Identificação de problemas persistentes

## 📦 Comandos Disponíveis

### `context-guide init [--project-type TIPO]`
Inicializa a estrutura de documentação em um projeto existente.
Tipos disponíveis: minimal, standard, complete, web, mobile, desktop.

### `context-guide update`
Atualiza manualmente o índice de contexto.

### `context-guide serve`
Inicia um servidor que monitora alterações nos arquivos Markdown e atualiza automaticamente o índice.

### `context-guide mcp [--host HOST] [--port PORTA] [--reload]`
Inicia o servidor MCP (Model Control Panel) para integração com o Cursor IDE.
- `--host` - Endereço para o servidor (padrão: 0.0.0.0)
- `--port` - Porta para o servidor (padrão: 8000)
- `--reload` - Ativa o recarregamento automático durante desenvolvimento

### `context-guide generate "Solicitação aqui"`
Gera um prompt enriquecido com contexto e copia para a área de transferência.

### Opções globais
- `--docs-dir PASTA` - Especifica a pasta de documentos (padrão: `docs`)
- `--db-dir PASTA` - Especifica a pasta para o banco de dados (padrão: `.context_guide`)

## 🔌 Integração com o Cursor IDE via MCP

O Context Guide agora oferece integração direta com o Cursor IDE através do MCP (Model Control Panel), permitindo consultas de contexto diretamente da IDE.

### Instalação das dependências do MCP

```bash
# Instalar o Context Guide com suporte a MCP
pip install "context-guide[mcp]"

# Ou, se já instalou, adicione as dependências
pip install fastapi uvicorn pydantic requests
```

### Iniciando o servidor MCP

```bash
# Iniciar o servidor MCP na porta padrão (8000)
context-guide mcp

# Personalizar host e porta
context-guide mcp --host 127.0.0.1 --port 8080
```

### Configuração da integração com o Cursor IDE

1. Obtenha um token de API do Cursor (acessível nas configurações da IDE)
2. Configure a variável de ambiente `CURSOR_API_TOKEN` com seu token
3. Use a API do servidor MCP para consultar contexto:

```bash
# Enviar consulta para o servidor MCP
curl -X POST http://localhost:8000/context \
  -H "Content-Type: application/json" \
  -d '{"query": "Como implementar autenticação no projeto?"}'

# Gerar prompt completo
curl -X POST http://localhost:8000/prompt \
  -H "Content-Type: application/json" \
  -d '{"request": "Criar componente de login"}'
```

### Endpoints disponíveis no servidor MCP

- `GET /` - Verificar status do servidor
- `POST /context` - Obter contexto relevante para uma consulta
- `POST /prompt` - Gerar prompt completo para uma solicitação
- `POST /update-index` - Atualizar índice de documentos

### Exemplo de utilização programática

```python
from context_guide.mcp_server.cursor_integration import CursorIntegration

# Inicializar integração (certifique-se que o servidor MCP está rodando)
cursor = CursorIntegration(mcp_url="http://localhost:8000")

# Enviar contexto diretamente para o Cursor IDE
query = "Como implementar autenticação no projeto?"
context_data = cursor.get_context_for_query(query)
cursor.send_context_to_cursor(context_data["context"])

# Ou melhorar um prompt diretamente
cursor.enhance_cursor_prompt("Criar novo componente de login com validação")
```

## 🌟 Fluxo de Trabalho para Desenvolvimento com AI

### 1. Configuração Inicial
- Execute `context-guide init --project-type complete` (ou escolha o tipo que melhor se adapta)
- Preencha os templates com informações do seu projeto

### 2. Acompanhamento Contínuo
- Mantenha os arquivos de tracking atualizados durante o desenvolvimento
- Use o arquivo `tracking/tasks.md` para acompanhar o progresso
- Registre falhas e sucessos em `tracking/modules-status.md` e `tracking/testing-status.md`

### 3. Geração de Código com Contexto (usando área de transferência)
- Execute o servidor de monitoramento: `context-guide serve`
- Gere prompts para o Cursor IDE: `context-guide generate "sua solicitação"`
- Use o contexto para corrigir erros: `context-guide generate "corrigir erro no módulo X"`

### 4. Geração de Código com Contexto (usando MCP)
- Inicie o servidor MCP: `context-guide mcp`
- Configure o token de API do Cursor: `export CURSOR_API_TOKEN="seu-token-aqui"`
- Use a integração programática ou os endpoints API para enviar contexto diretamente ao Cursor

### 5. Documentação Evolutiva
- Atualize a documentação à medida que o projeto cresce
- Mantenha a arquitetura em sincronia com a implementação
- Adicione novos componentes e features aos respectivos documentos

## 🔧 Para Desenvolvedores

### Ambiente de desenvolvimento

```bash
# Clone o repositório
git clone https://github.com/seuusuario/context-guide.git
cd context-guide

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instale em modo de desenvolvimento
pip install -e .
```

### Empacotamento para distribuição

```bash
# Instale as ferramentas de build
pip install build twine

# Crie o pacote distribuível
python -m build

# Publique no PyPI (substitua por TestPyPI para testes)
python -m twine upload dist/*
```

## 📝 Notas

- O sistema utiliza apenas embeddings locais para melhor desempenho e privacidade
- Recomenda-se manter os documentos Markdown concisos e bem organizados para facilitar a recuperação de contexto
- O banco de dados é armazenado localmente em `.context_guide/` (já configurado para ser ignorado pelo Git)

## 📄 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).