# Context Guide

**Context Guide** é uma ferramenta poderosa para fornecer contexto automático ao Cursor IDE e outras IDEs assistidas por IA, ajudando a evitar perda de contexto e alucinações em projetos de qualquer linguagem.

## ⭐ Recursos Principais

- **Markdown como fonte única de contexto**: Documentação em arquivos simples
- **RAG via LlamaIndex e ChromaDB**: Indexação e busca eficiente por embeddings
- **Compatível com qualquer projeto/linguagem**: Funciona independentemente da linguagem do projeto
- **Atualização automática em tempo real**: Detecta alterações nos arquivos Markdown e atualiza o índice
- **Geração de prompts enriquecidos**: Consulta automática do contexto relevante antes de gerar código
- **Fácil integração**: Copia o prompt para a área de transferência para uso no Cursor IDE

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

# Inicialize a estrutura de documentação
context-guide init
```

### 2. Atualize os arquivos Markdown com informações do seu projeto

Edite os arquivos criados na pasta `docs/`:
- `overview.md` - Visão geral do projeto
- `components.md` - Componentes do sistema
- `features.md` - Funcionalidades implementadas
- `architecture.md` - Detalhes técnicos da arquitetura

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

## 📚 Comandos Disponíveis

### `context-guide init`
Inicializa a estrutura de documentação em um projeto existente.

### `context-guide update`
Atualiza manualmente o índice de contexto.

### `context-guide serve`
Inicia um servidor que monitora alterações nos arquivos Markdown e atualiza automaticamente o índice.

### `context-guide generate "Solicitação aqui"`
Gera um prompt enriquecido com contexto e copia para a área de transferência.

### Opções globais
- `--docs-dir PASTA` - Especifica a pasta de documentos (padrão: `docs`)
- `--db-dir PASTA` - Especifica a pasta para o banco de dados (padrão: `.context_guide`)

## 🌟 Fluxo de Trabalho Recomendado

1. **Documentação do projeto**: Mantenha os arquivos Markdown atualizados com informações sobre componentes, arquitetura e funcionalidades do seu projeto.

2. **Iniciar o servidor**: Execute `context-guide serve` em um terminal dedicado para monitorar alterações nos documentos.

3. **Gerar código com contexto**: Quando precisar gerar código no Cursor IDE, use `context-guide generate "sua solicitação"` e cole o prompt resultante no Cursor.

4. **Iteração contínua**: À medida que o projeto evolui, atualize os arquivos Markdown para manter o contexto preciso.

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