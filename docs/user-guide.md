# Guia do Usuário do Context Guide

## Introdução

O Context Guide é uma ferramenta inovadora projetada para melhorar drasticamente a experiência de desenvolvimento com IDEs assistidas por IA, como o Cursor. Ao fornecer contexto rico e específico do projeto para os modelos de IA, o Context Guide ajuda a obter respostas mais precisas e alinhadas com a base de código de seu projeto.

## Por que usar o Context Guide?

As IDEs assistidas por IA frequentemente sofrem de:

1. **Falta de contexto específico do projeto** - A IA não conhece automaticamente a arquitetura, padrões e convenções do seu projeto
2. **Janela de contexto limitada** - Os modelos têm limite de tokens, não podendo processar toda a base de código
3. **Alucinações e inconsistências** - Respostas genéricas que não se alinham com o código existente

O Context Guide resolve esses problemas ao:

- Manter um índice pesquisável da documentação do projeto
- Recuperar automaticamente informações relevantes para suas solicitações
- Formatar prompts enriquecidos que fornecem o contexto exato necessário

## Instalação

### Requisitos

- Python 3.9 ou superior
- Pip (gerenciador de pacotes Python)
- Acesso ao Cursor IDE (opcional, para integração completa)

### Procedimento de Instalação

```bash
# Instalação básica
pip install context-guide

# Instalação com suporte a MCP (recomendado)
pip install "context-guide[mcp]"
```

Para verificar a instalação:

```bash
context-guide --help
```

## Primeiros Passos

### Inicialização do Projeto

O primeiro passo é inicializar a estrutura de documentação:

```bash
# Navegue até a raiz do seu projeto
cd seu-projeto

# Inicialize a estrutura básica de documentação
context-guide init
```

Este comando criará uma pasta `docs/` com vários arquivos Markdown que servirão como fonte de verdade para o Context Guide.

### Tipos de Projeto

Escolha o tipo de projeto que melhor se adapta às suas necessidades:

```bash
# Para um projeto web
context-guide init --project-type web

# Para um projeto mobile
context-guide init --project-type mobile

# Para um projeto desktop
context-guide init --project-type desktop

# Para documentação mínima
context-guide init --project-type minimal

# Para documentação completa
context-guide init --project-type complete
```

### Preenchendo a Documentação

Após a inicialização, você deve editar os arquivos Markdown gerados para adicionar informações específicas do seu projeto. Concentre-se inicialmente nos seguintes arquivos:

1. `docs/overview.md` - Visão geral, propósito e tecnologias do projeto
2. `docs/architecture.md` - Arquitetura, padrões de design e estrutura
3. `docs/components.md` - Componentes principais e suas responsabilidades
4. `docs/features.md` - Funcionalidades e requisitos implementados

Exemplo de `overview.md` bem preenchido:

```markdown
# Visão Geral do Projeto

## Propósito
Este projeto é um sistema de gerenciamento de biblioteca que permite aos usuários pesquisar, emprestar e devolver livros. O sistema também oferece funcionalidades administrativas para gerenciar o acervo.

## Tecnologias Principais
- Frontend: React com TypeScript e Material UI
- Backend: Node.js com Express e TypeScript
- Banco de dados: PostgreSQL com Prisma ORM
- Autenticação: JWT com refresh tokens

## Arquitetura Geral
O sistema segue uma arquitetura de microserviços, com serviços separados para:
- Autenticação e gerenciamento de usuários
- Catálogo de livros
- Empréstimos e devoluções
- Notificações
```

### Criando o Índice

Depois de preencher a documentação, crie o índice:

```bash
context-guide update
```

Este comando processará todos os arquivos Markdown em `docs/` e criará um índice pesquisável que será usado para recuperar informações contextuais.

## Uso Diário

### Monitoramento Automático

Para manter o índice atualizado enquanto você trabalha na documentação:

```bash
context-guide serve
```

Este comando inicia um servidor que monitora alterações nos arquivos Markdown e atualiza o índice automaticamente.

### Gerando Prompts Enriquecidos

Quando precisar gerar código com o Cursor IDE:

```bash
# Formato básico
context-guide generate "Criar componente de formulário de login"

# Com contexto tecnológico específico
context-guide generate "Criar componente de formulário de login" --technology react
```

O prompt gerado será copiado para a área de transferência. Cole-o diretamente no Cursor IDE para obter código que respeita o contexto do seu projeto.

## Integração Avançada com o Cursor IDE via MCP

Para uma experiência mais integrada, o Context Guide oferece o servidor MCP (Model Control Panel) que pode se comunicar diretamente com o Cursor IDE.

### Configuração do Servidor MCP

```bash
# Iniciar o servidor MCP na porta padrão (8000)
context-guide mcp

# Personalizar host e porta
context-guide mcp --host 127.0.0.1 --port 8080 --reload
```

### Configurando a Integração com o Cursor

1. Obtenha um token de API do Cursor IDE:
   - Abra o Cursor IDE
   - Vá para Configurações (ícone de engrenagem)
   - Navegue até a seção API
   - Gere um novo token de API
   - Copie o token gerado

2. Configure a variável de ambiente:

```bash
# Linux/macOS
export CURSOR_API_TOKEN="seu-token-aqui"

# Windows (PowerShell)
$env:CURSOR_API_TOKEN="seu-token-aqui"
```

3. Verifique a configuração:

```bash
# Este comando deve retornar "Servidor MCP está saudável" se tudo estiver configurado corretamente
curl http://localhost:8000/health
```

### Usando a API

Uma vez que o servidor MCP esteja em execução, você pode interagir com ele via API:

#### Obter Contexto para uma Consulta

```bash
curl -X POST http://localhost:8000/context \
  -H "Content-Type: application/json" \
  -d '{"query": "Como implementar o login?", "technology_context": "node"}'
```

#### Gerar um Prompt Enriquecido

```bash
curl -X POST http://localhost:8000/prompt \
  -H "Content-Type: application/json" \
  -d '{"request": "Implementar middleware de autenticação", "technology_context": "node"}'
```

#### Enviar Contexto Diretamente para o Cursor

Para isso, você precisará usar a biblioteca Python:

```python
from context_guide.mcp_server.cursor_integration import CursorIntegration

# Inicializar a integração
cursor = CursorIntegration()

# Enviar um prompt enriquecido para o Cursor
cursor.enhance_cursor_prompt("Criar componente de tabela de dados", technology="react")
```

## Trabalhando com Tecnologias Específicas

O Context Guide oferece suporte otimizado para diversas tecnologias, enriquecendo o contexto com informações específicas para cada stack.

### React

```bash
context-guide generate "Criar componente Card reutilizável" --technology react
```

Isso enriquecerá o prompt com informações sobre:
- Componentes funcionais e hooks
- Padrões de estado e props
- Melhores práticas de React

### Node.js

```bash
context-guide generate "Implementar middleware de autenticação" --technology node
```

O contexto incluirá:
- Padrões de middleware
- Estruturação de rotas e controladores
- Melhores práticas para Express/Node

### Django

```bash
context-guide generate "Criar modelo para gerenciamento de usuários" --technology django
```

Enriquecido com:
- Padrão MVT (Model-View-Template)
- Uso apropriado de models e forms
- Integração com o Django Admin

### Flask

```bash
context-guide generate "Implementar blueprint para API REST" --technology flask
```

### Vue.js

```bash
context-guide generate "Criar componente de navegação" --technology vue
```

### Spring Boot

```bash
context-guide generate "Criar controlador REST" --technology spring
```

## Organização da Documentação

Para projetos maiores, recomendamos organizar a documentação por domínios:

```
docs/
├── core/
│   ├── overview.md
│   └── architecture.md
├── frontend/
│   ├── components.md
│   └── styling-guide.md
├── backend/
│   ├── api.md
│   └── database-schema.md
├── dev-ops/
│   ├── deployment.md
│   └── monitoring.md
└── tracking/
    ├── tasks.md
    └── modules-status.md
```

O Context Guide processará automaticamente toda a estrutura de arquivos.

## Fluxo de Trabalho em Equipe

Para equipes, recomendamos:

1. **Incluir a documentação no controle de versão**: Adicione a pasta `docs/` ao Git
2. **Excluir o banco de dados do controle de versão**: Adicione `.context_guide/` ao `.gitignore`
3. **Automatizar atualizações**: Execute `context-guide update` após pulls ou merges
4. **Servidor MCP compartilhado**: Configure um servidor MCP em um ambiente compartilhado
5. **Revisão de documentação**: Inclua a documentação no processo de code review

## Solução de Problemas

### O prompt gerado não inclui o contexto esperado

**Possível causa**: A documentação não contém as informações necessárias ou não está indexada.

**Solução**:
1. Verifique se a documentação relevante existe e está detalhada
2. Execute `context-guide update` para reindexar
3. Torne sua consulta mais específica

### Erro ao iniciar o servidor MCP

**Possível causa**: Dependências não instaladas.

**Solução**:
```bash
pip install "context-guide[mcp]"
```

### Falha na integração com o Cursor IDE

**Possível causa**: Token de API incorreto ou não configurado.

**Solução**:
1. Verifique se o token está configurado corretamente
2. Teste a conexão com `curl http://localhost:8000/health`
3. Verifique os logs do servidor MCP

## Dicas e Truques

### Prompts Eficazes

Para obter melhores resultados:

1. **Seja específico**: "Criar componente de tabela com paginação e filtros" é melhor que "Fazer componente de tabela"
2. **Mencione padrões**: "Seguindo o padrão repositório" ajuda a gerar código consistente
3. **Especifique a tecnologia**: Use a opção `--technology` para contexto mais preciso

### Otimização de Desempenho

Para projetos grandes:

1. **Divida a documentação**: Use uma estrutura hierárquica para organizar documentos
2. **Seja conciso**: Prefira documentação específica e focada em vez de textos longos
3. **Atualize seletivamente**: Use `context-guide update --docs-dir subpasta` para atualizar apenas seções específicas

## Conclusão

O Context Guide transforma sua experiência com IDEs assistidas por IA, fornecendo contexto rico e específico do projeto. Ao manter uma documentação de qualidade e usar os prompts gerados, você obterá código mais alinhado com a arquitetura, padrões e convenções do seu projeto, economizando tempo e reduzindo frustrações com respostas genéricas ou incorretas.

Explore recursos adicionais e contribua para o projeto em [GitHub](https://github.com/DiegoNogueiraDev/context-guide). 