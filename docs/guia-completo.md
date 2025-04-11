# Guia Completo do Context Guide

Este documento é um guia detalhado para instalação, configuração e uso do Context Guide, uma ferramenta projetada para fornecer contexto automático para IDEs assistidas por IA.

## Sumário

1. [Visão Geral](#visão-geral)
2. [Instalação](#instalação)
3. [Configuração Inicial](#configuração-inicial)
4. [Comandos e Funcionalidades](#comandos-e-funcionalidades)
5. [Estrutura de Documentação](#estrutura-de-documentação)
6. [Melhores Práticas](#melhores-práticas)
7. [Resolução de Problemas](#resolução-de-problemas)
8. [Exemplos Práticos](#exemplos-práticos)
9. [Recursos Avançados](#recursos-avançados)

## Visão Geral

Context Guide é uma ferramenta que resolve o problema de falta de contexto ao trabalhar com IDEs assistidas por IA (como Cursor). A ferramenta mantém um índice de documentação em Markdown e gera prompts enriquecidos com contexto relevante para suas solicitações.

### Principais Recursos

- **Documentação em Markdown**: Mantém toda a documentação em arquivos simples e legíveis
- **Indexação por Embeddings**: Usa LlamaIndex e ChromaDB para criar índices eficientes
- **Geração Contextualizada**: Recupera contexto relevante automaticamente
- **Monitoramento em Tempo Real**: Detecta alterações e atualiza o índice
- **Templates para Projetos**: Oferece estruturas pré-definidas para vários tipos de projeto

## Instalação

### Requisitos do Sistema

- Python 3.9 ou superior
- Pip (gerenciador de pacotes do Python)
- Ambiente Linux, macOS ou Windows

### Instalação via pip

A maneira mais simples de instalar o Context Guide é usando o pip:

```bash
pip install context-guide
```

### Instalação a partir do Código Fonte

Para instalar a versão mais recente do código:

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/context-guide.git
   cd context-guide
   ```

2. Instale em modo de desenvolvimento:
   ```bash
   pip install -e .
   ```

### Dependências para Linux

Se você estiver usando Linux, pode ser necessário instalar o `xclip` para que a funcionalidade de clipboard funcione:

```bash
sudo apt-get install xclip
# ou
sudo apt-get install xsel
```

### Verificação da Instalação

Para verificar se a instalação foi bem-sucedida:

```bash
context-guide --help
```

Você deverá ver o menu de ajuda com os comandos disponíveis.

## Configuração Inicial

### Inicializando um Projeto

O primeiro passo é inicializar a estrutura de documentação em seu projeto:

```bash
# Navegue até a pasta do seu projeto
cd meu-projeto

# Inicialize com a estrutura padrão
context-guide init
```

### Tipos de Projetos Disponíveis

O Context Guide oferece diferentes modelos de documentação para diversas necessidades:

```bash
# Estrutura mínima (apenas documentos básicos)
context-guide init --project-type minimal

# Estrutura padrão (documentos básicos + acompanhamento)
context-guide init --project-type standard

# Estrutura completa (todos os documentos)
context-guide init --project-type complete

# Estrutura específica para aplicações web
context-guide init --project-type web

# Estrutura específica para aplicações mobile
context-guide init --project-type mobile

# Estrutura específica para aplicações desktop
context-guide init --project-type desktop
```

### Personalizando a Localização dos Documentos

Por padrão, os documentos são armazenados na pasta `docs/` e o banco de dados em `.context_guide/`. Você pode personalizar essas localizações:

```bash
context-guide init --docs-dir minha-documentacao
context-guide update --docs-dir minha-documentacao --db-dir meu-banco-de-dados
```

## Comandos e Funcionalidades

### Atualizando o Índice

Após preencher seus documentos, atualize o índice:

```bash
context-guide update
```

### Monitoramento Automático

Para iniciar o servidor de monitoramento que detecta alterações nos arquivos:

```bash
context-guide serve
```

O servidor continuará rodando até que você pressione Ctrl+C para interrompê-lo.

### Gerando Prompts

Para gerar um prompt enriquecido com contexto:

```bash
context-guide generate "Criar componente de login com validação de email"
```

O prompt gerado será automaticamente copiado para sua área de transferência e poderá ser colado diretamente no Cursor IDE.

### Opções Avançadas de Geração

Você pode personalizar o processo de geração:

```bash
# Especificando um diretório de documentos diferente
context-guide generate "Implementar funcionalidade X" --docs-dir outra-pasta

# Especificando um diretório de banco de dados diferente
context-guide generate "Implementar funcionalidade X" --db-dir outro-db
```

## Estrutura de Documentação

### Estrutura Padrão

A estrutura padrão criada pelo comando `init` inclui:

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
└── architecture/             # Arquiteturas específicas
    ├── web-app.md            # Para aplicações web
    ├── mobile-app.md         # Para aplicações mobile
    └── desktop-app.md        # Para aplicações desktop
```

### Documentos Básicos

Os documentos básicos contêm informações fundamentais sobre o projeto:

| Arquivo | Propósito |
|---------|-----------|
| `overview.md` | Visão geral, propósito, tecnologias principais |
| `architecture.md` | Estrutura técnica, padrões arquiteturais |
| `components.md` | Componentes reutilizáveis, interfaces |
| `features.md` | Funcionalidades implementadas e planejadas |

### Documentos de Acompanhamento

Os documentos de acompanhamento servem para rastrear o progresso:

| Arquivo | Propósito |
|---------|-----------|
| `tracking/tasks.md` | Lista de tarefas, andamento, bloqueios |
| `tracking/modules-status.md` | Status de cada módulo, problemas conhecidos |
| `tracking/testing-status.md` | Resultados de testes, cobertura |

### Documentos de Desenvolvimento

Os documentos de desenvolvimento contêm guias e padrões:

| Arquivo | Propósito |
|---------|-----------|
| `development/api-docs.md` | Documentação de endpoints e modelos |
| `development/best-practices.md` | Padrões de código e arquitetura |
| `development/tools-environment.md` | Ferramentas e ambiente de desenvolvimento |
| `development/deployment.md` | Processos de build e implantação |

## Melhores Práticas

### Preenchendo os Templates

Para obter o máximo de benefícios:

1. **Seja específico**: Inclua detalhes concretos sobre componentes e arquitetura
2. **Mantenha atualizado**: Atualize a documentação à medida que o projeto evolui
3. **Use exemplos**: Inclua exemplos de código onde relevante
4. **Compartilhe decisões**: Documente as razões por trás das decisões arquiteturais

### Dicas para Gerar Melhores Prompts

1. **Seja claro em suas solicitações**: "Criar componente Button com variantes de tamanho" é melhor que "Fazer botão"
2. **Referencie componentes existentes**: "Usar o formato do componente Header" fornece contexto adicional
3. **Mencione restrições**: "Seguindo o padrão de acessibilidade WCAG" ajuda a obter resultados adequados

### Fluxo de Trabalho Recomendado

1. **Inicialize o projeto**: `context-guide init --project-type [tipo]`
2. **Preencha a documentação**: Atualize os arquivos Markdown
3. **Atualize o índice**: `context-guide update`
4. **Execute o servidor**: `context-guide serve` (em um terminal separado)
5. **Gere prompts**: `context-guide generate "Sua solicitação"`
6. **Use no Cursor**: Cole o prompt gerado no Cursor IDE
7. **Atualize documentação**: Conforme implementa novas funcionalidades

## Resolução de Problemas

### Problemas Comuns e Soluções

| Problema | Solução |
|----------|---------|
| `ModuleNotFoundError` para llama_index | Execute `pip install llama-index==0.9.0 chromadb==0.4.18` |
| Erro ao copiar para clipboard | Instale xclip: `sudo apt-get install xclip` |
| Contexto irrelevante recuperado | Torne sua documentação mais específica e organizada |
| Índice não atualiza | Reinicie o servidor com `context-guide serve` |

### Verificação de Dependências

Se estiver tendo problemas com dependências:

```bash
pip list | grep llama-index
pip list | grep chromadb
pip list | grep pyperclip
```

### Limpeza e Reinicialização

Para recomeçar do zero:

```bash
rm -rf .context_guide
context-guide update
```

## Exemplos Práticos

### Exemplo 1: Desenvolvimento Web com Context Guide

```bash
# Inicializar projeto
mkdir meu-app-web
cd meu-app-web
context-guide init --project-type web

# Preencher documentação 
# (Edite arquivos em docs/)

# Atualizar índice
context-guide update

# Gerar prompt para componente
context-guide generate "Criar componente Navbar responsivo com links para Home, Produtos e Contato"
```

### Exemplo 2: Desenvolvimento Mobile

```bash
# Inicializar projeto
mkdir meu-app-mobile
cd meu-app-mobile
context-guide init --project-type mobile

# Preencher documentação
# (Edite arquivos em docs/)

# Atualizar índice
context-guide update

# Gerar prompt para uma tela
context-guide generate "Implementar tela de perfil de usuário com foto, informações básicas e botão de edição"
```

### Exemplo 3: Guia para Agentes IA

```bash
# Para projetos complexos trabalhando com múltiplos agentes IA
mkdir projeto-ai-agents
cd projeto-ai-agents
context-guide init --project-type complete

# Documentação muito detalhada é crucial aqui
# (Edite arquivos em docs/ - seja minucioso)

# Atualizar índice
context-guide update

# Iniciar servidor em terminal separado
context-guide serve

# Em outro terminal, gerar prompt para um agente
context-guide generate "Implementar módulo de autenticação seguindo a arquitetura hexagonal conforme documentado"
```

## Recursos Avançados

### Personalização de Templates

Você pode personalizar os templates editando os arquivos manualmente após a inicialização.

### Uso com Diferentes IDEs

Embora projetado para o Cursor IDE, o Context Guide pode ser usado com qualquer IDE ou editor que aceite prompts de texto. Simplesmente cole o prompt gerado no ambiente de sua escolha.

### Integração com Fluxos de Trabalho

O Context Guide pode ser incorporado em fluxos de trabalho de CI/CD:

```bash
# Exemplo de uso em um script de CI/CD
context-guide update
context-guide generate "Revisar código para garantir que segue os padrões documentados" > review-prompt.txt
```

### Uso em Equipes

Para equipes, a abordagem recomendada é:

1. Inicializar o projeto e incluir os arquivos de documentação no controle de versão
2. Cada membro da equipe instala o Context Guide localmente
3. O `.context_guide/` (banco de dados) deve estar no `.gitignore`
4. Todos mantêm o índice atualizado localmente com `context-guide update`
5. A documentação evolui junto com o código

---

## Notas Adicionais

- O Context Guide não envia nenhum dado para servidores externos
- Todo o processamento ocorre localmente em sua máquina
- A performance pode variar dependendo do tamanho da documentação

Para mais informações, consulte o [README.md](../README.md) e o [guia para desenvolvedores](development-guide.md). 