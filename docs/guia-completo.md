# Guia Completo do Context Guide

## O que é o Context Guide?

O Context Guide é uma ferramenta inovadora projetada para fornecer contexto automatizado para IDEs assistidas por IA, como o Cursor. A ferramenta resolve um dos principais problemas enfrentados ao utilizar assistentes de IA para desenvolvimento: a falta de contexto específico do projeto, o que muitas vezes leva a sugestões genéricas ou incoerentes com a base de código existente.

Utilizando documentação em Markdown como fonte única de verdade e técnicas avançadas de RAG (Retrieval Augmented Generation) com LlamaIndex e ChromaDB, o Context Guide indexa sua documentação e a disponibiliza de forma contextualizada quando você precisa gerar código.

## Recursos Principais

- **Markdown como fonte de contexto**: Utiliza documentação em arquivos simples, fáceis de manter
- **RAG via LlamaIndex e ChromaDB**: Indexação e busca eficiente por embeddings
- **Compatibilidade universal**: Funciona com qualquer linguagem de programação ou tipo de projeto
- **Monitoramento em tempo real**: Detecta alterações e atualiza o índice automaticamente
- **Geração de prompts enriquecidos**: Consulta automática do contexto relevante para gerar código
- **Templates abrangentes**: Modelos para todos os aspectos da documentação do projeto
- **Rastreamento de progresso**: Monitoramento de tarefas, módulos e testes
- **Integração com Cursor IDE**: API para envio direto de contexto via MCP

## Instalação Detalhada

### Requisitos do Sistema

- Python 3.9 ou superior
- Pip (gerenciador de pacotes Python)
- 500MB de espaço em disco para o Chroma DB (depende do tamanho da documentação)

### Instalação via pip

```bash
# Instalação básica
pip install context-guide

# Instalação com suporte a MCP (recomendado)
pip install "context-guide[mcp]"
```

### Instalação a partir do código-fonte

```bash
# Clone o repositório
git clone https://github.com/DiegoNogueiraDev/context-guide.git
cd context-guide

# Instalação básica
pip install -e .

# Instalação com suporte a MCP (recomendado)
pip install -e ".[mcp]"
```

### Verificação da instalação

Confirme se a instalação foi bem-sucedida executando:

```bash
context-guide --help
```

Você deverá ver a ajuda do Context Guide com a lista de comandos disponíveis.

## Uso Detalhado

### 1. Inicialização do Projeto

O primeiro passo é inicializar a estrutura de documentação no seu projeto:

```bash
# Navegue até a pasta do seu projeto
cd meu-projeto

# Inicialize com a configuração padrão
context-guide init

# Para inicializar com configuração específica
context-guide init --project-type web  # Opções: minimal, standard, complete, web, mobile, desktop
```

Este comando criará uma pasta `docs/` no seu projeto com arquivos Markdown estruturados conforme o tipo de projeto escolhido.

#### Opções de inicialização

| Tipo      | Descrição                                            | Uso recomendado                    |
|-----------|------------------------------------------------------|-----------------------------------|
| minimal   | Apenas documentos básicos                            | Projetos pequenos ou pessoais     |
| standard  | Documentos básicos + acompanhamento (padrão)         | Projetos de médio porte           |
| complete  | Todos os documentos                                  | Projetos complexos                 |
| web       | Complete + templates específicos para web            | Aplicações web                     |
| mobile    | Complete + templates específicos para mobile         | Aplicações móveis                  |
| desktop   | Complete + templates específicos para desktop        | Aplicações desktop                 |

### 2. Personalização da Documentação

Edite os arquivos Markdown gerados para adicionar informações específicas do seu projeto. Recomendamos manter a documentação:

- **Concisa**: Documentos mais curtos são mais fáceis de manter e atualizar
- **Estruturada**: Mantenha a estrutura original para facilitar a recuperação
- **Específica**: Foque em detalhes técnicos que ajudarão a IA a entender seu projeto
- **Atualizada**: Atualize regularmente conforme o projeto evolui

Os arquivos principais que você deve editar primeiro são:
- `docs/overview.md` - Visão geral do projeto
- `docs/architecture.md` - Arquitetura e componentes principais
- `docs/features.md` - Funcionalidades e requisitos do sistema

### 3. Indexação da Documentação

Após editar a documentação, você precisa indexá-la:

```bash
context-guide update
```

Este comando:
1. Lê todos os arquivos Markdown na pasta `docs/`
2. Cria embeddings usando o modelo especificado
3. Armazena os embeddings no ChromaDB em `.context_guide/`

### 4. Acompanhamento Contínuo (opcional)

Para manter o índice atualizado automaticamente enquanto você edita a documentação:

```bash
context-guide serve
```

Este comando inicia um servidor que monitora alterações nos arquivos Markdown e atualiza o índice automaticamente. Ideal para uso durante o desenvolvimento ativo.

### 5. Geração de Prompts Contextualizados

Para gerar um prompt enriquecido com contexto para o Cursor IDE:

```bash
# Formato básico
context-guide generate "Criar componente de login com validação"

# Especificando tecnologia
context-guide generate "Criar componente de login com validação" --technology react
```

O prompt gerado será automaticamente copiado para a área de transferência. Você pode então colá-lo diretamente no Cursor IDE.

## Integração MCP com Cursor IDE

O Context Guide oferece integração avançada com o Cursor IDE através do MCP (Model Control Panel), permitindo consultas de contexto diretamente da IDE.

### 1. Configuração do Servidor MCP

Primeiro, inicie o servidor MCP:

```bash
# Configuração básica (porta 8000)
context-guide mcp

# Configuração personalizada
context-guide mcp --host 127.0.0.1 --port 8080 --reload
```

Opções disponíveis:
- `--host`: Endereço IP para o servidor (padrão: 0.0.0.0)
- `--port`: Porta para o servidor (padrão: 8000)
- `--reload`: Ativa o recarregamento automático durante desenvolvimento

### 2. Configuração da API do Cursor

Para usar a integração direta com o Cursor IDE, você precisa configurar um token de API:

1. Abra o Cursor IDE
2. Acesse Configurações → Geral → API
3. Gere um novo token de API
4. Configure a variável de ambiente:

```bash
# Linux/macOS
export CURSOR_API_TOKEN="seu-token-aqui"

# Windows (CMD)
set CURSOR_API_TOKEN=seu-token-aqui

# Windows (PowerShell)
$env:CURSOR_API_TOKEN="seu-token-aqui"

# Para tornar permanente, adicione ao seu .bashrc, .zshrc, etc.
echo 'export CURSOR_API_TOKEN="seu-token-aqui"' >> ~/.bashrc
```

### 3. Uso da API MCP

O servidor MCP oferece endpoints RESTful para interagir com o Context Guide:

#### Verificação de Status

```bash
curl http://localhost:8000/
```

#### Obtenção de Contexto

```bash
curl -X POST http://localhost:8000/context \
  -H "Content-Type: application/json" \
  -d '{"query": "Como implementar autenticação?", "num_results": 5, "technology_context": "react"}'
```

#### Geração de Prompt

```bash
curl -X POST http://localhost:8000/prompt \
  -H "Content-Type: application/json" \
  -d '{"request": "Criar componente de login", "technology_context": "react", "include_best_practices": true}'
```

#### Atualização do Índice

```bash
curl -X POST http://localhost:8000/update-index
```

#### Estatísticas do Servidor

```bash
curl http://localhost:8000/stats
```

#### Verificação de Saúde

```bash
curl http://localhost:8000/health
```

### 4. Integração Programática

Você também pode integrar o Context Guide programaticamente em seus scripts:

```python
from context_guide.mcp_server.cursor_integration import CursorIntegration

# Inicializar com servidor MCP local
cursor = CursorIntegration(mcp_url="http://localhost:8000")

# Verificar se o servidor está saudável
if cursor.check_server_health():
    # Enviar contexto diretamente para o Cursor IDE
    query = "Como implementar autenticação JWT?"
    context_data = cursor.get_context_for_query(query, technology="node")
    cursor.send_context_to_cursor(context_data["context"], technology="node")
    
    # Alternativa: usar um prompt enriquecido
    cursor.enhance_cursor_prompt(
        "Criar rota de login com validação", 
        technology="node",
        include_best_practices=True
    )
    
    # Atualizar o índice
    cursor.update_index()
    
    # Obter estatísticas
    stats = cursor.get_server_stats()
    print(f"Total de requisições: {stats.get('total_requests', 0)}")
```

## Suporte a Tecnologias Específicas

O Context Guide oferece suporte especial para as seguintes tecnologias:

| Tecnologia | Descrição                                    | Padrões Suportados                                 |
|------------|----------------------------------------------|---------------------------------------------------|
| react      | Biblioteca JavaScript para UIs               | Componentes funcionais, hooks, estados, contexto   |
| node       | Ambiente JavaScript para servidor            | Middleware, rotas, controladores, modelos          |
| django     | Framework web Python de alto nível           | Views, models, templates, forms, admin             |
| flask      | Microframework web Python                    | Rotas, blueprints, extensões, contexto             |
| vue        | Framework JavaScript progressivo para UIs    | Componentes, diretivas, props, composition API     |
| spring     | Framework Java para desenvolvimento          | Controladores, serviços, repositórios, entidades   |

Para usar o suporte a tecnologias específicas:

```bash
# Via linha de comando
context-guide generate "Criar componente de login" --technology react

# Via API
curl -X POST http://localhost:8000/prompt \
  -H "Content-Type: application/json" \
  -d '{"request": "Criar componente de login", "technology_context": "react"}'
```

Isso enriquecerá o prompt com informações específicas sobre a tecnologia, incluindo melhores práticas e padrões comuns.

## Configurações Avançadas

### Variáveis de Ambiente

O Context Guide suporta as seguintes variáveis de ambiente:

| Variável                | Descrição                                | Valor Padrão        |
|-------------------------|------------------------------------------|--------------------|
| CURSOR_API_TOKEN        | Token de API para o Cursor IDE           | (nenhum)           |
| CONTEXT_GUIDE_DOCS_DIR  | Diretório de documentação                | docs               |
| CONTEXT_GUIDE_DB_DIR    | Diretório para o banco de dados          | .context_guide     |
| CONTEXT_GUIDE_LOG_LEVEL | Nível de log (INFO, DEBUG, etc.)         | INFO               |
| CONTEXT_GUIDE_LOG_FILE  | Arquivo de log (opcional)                | (nenhum)           |

### Personalização do Logging

Você pode configurar o logging de forma avançada:

```bash
# Definir nível de log
export CONTEXT_GUIDE_LOG_LEVEL=DEBUG

# Definir arquivo de log
export CONTEXT_GUIDE_LOG_FILE=/var/log/context-guide.log

# Exemplo de uso combinado
CONTEXT_GUIDE_LOG_LEVEL=DEBUG CONTEXT_GUIDE_LOG_FILE=./logs/debug.log context-guide mcp
```

### Personalização do ChromaDB

Para projetos com muita documentação, você pode querer personalizar o ChromaDB:

```bash
# Diretório personalizado para o banco de dados
context-guide update --db-dir /path/para/db

# Usado em conjunto com comandos
context-guide generate "Criar API REST" --docs-dir ./documentacao --db-dir ./db
```

## Resolução de Problemas

### Erros Comuns

| Erro                                    | Possível Causa                             | Solução                                        |
|-----------------------------------------|--------------------------------------------|------------------------------------------------|
| ImportError ao iniciar o servidor MCP   | Dependências do MCP não instaladas         | `pip install "context-guide[mcp]"`             |
| Falha ao conectar ao servidor MCP       | Servidor não está em execução              | Inicie o servidor com `context-guide mcp`      |
| Erro de autorização no Cursor           | Token de API inválido ou não configurado   | Verifique o token e a variável de ambiente     |
| Documentação não atualizada no índice   | Índice não foi reconstruído após mudanças  | Execute `context-guide update`                 |
| Contexto irrelevante nas respostas      | Documentação de baixa qualidade            | Melhore a documentação com detalhes específicos|

### Logs de Depuração

Para problemas complexos, ative o log de depuração:

```bash
export CONTEXT_GUIDE_LOG_LEVEL=DEBUG
context-guide mcp --reload
```

Isso fornecerá informações detalhadas sobre o que está acontecendo internamente.

## Guia para Equipes

### Fluxo de Trabalho Recomendado

Para equipes de desenvolvimento, recomendamos o seguinte fluxo de trabalho:

1. **Instalação**: Todos os desenvolvedores instalam o Context Guide
2. **Inicialização**: Configurar a estrutura de documentação no início do projeto
3. **Colaboração**: Usar controle de versão (Git) para a pasta `docs/`
4. **Atualização**: Estabeleça um processo para manter a documentação atualizada
5. **Integração**: Configurar o servidor MCP em um ambiente compartilhado
6. **Automação**: Integrar com pipelines de CI/CD para atualização automática

### Dicas para Equipes Grandes

- **Documentação por Domínio**: Divida a documentação por domínios ou módulos
- **MCP Centralizado**: Considere executar o servidor MCP como um serviço compartilhado
- **Convenções**: Estabeleça convenções claras para a documentação
- **Revisão**: Incorpore revisão de documentação no processo de code review

## Contribuindo para o Context Guide

O Context Guide é um projeto de código aberto e agradecemos contribuições. Para contribuir:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Implemente suas mudanças
4. Execute os testes (`pytest`)
5. Envie um Pull Request

Para mais detalhes, consulte o arquivo [CONTRIBUTING.md](https://github.com/DiegoNogueiraDev/context-guide/blob/main/CONTRIBUTING.md).

## Recursos Adicionais

- [GitHub do Projeto](https://github.com/DiegoNogueiraDev/context-guide)
- [Documentação do LlamaIndex](https://docs.llamaindex.ai/)
- [Documentação do ChromaDB](https://docs.trychroma.com/)
- [API do Cursor IDE](https://cursor.sh/docs/api)

## Licença

Context Guide é distribuído sob a [Licença MIT](https://github.com/DiegoNogueiraDev/context-guide/blob/main/LICENSE). 