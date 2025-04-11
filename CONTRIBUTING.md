# Guia de Contribuição

Obrigado pelo interesse em contribuir com o Context Guide! Este documento fornece diretrizes para contribuir com o projeto.

## Como Contribuir

### Reportando Bugs

Se você encontrou um bug:

1. Verifique se o bug já foi reportado na seção de [Issues](https://github.com/DiegoNogueiraDev/context-guide/issues).
2. Se não encontrar uma issue aberta sobre o problema, [abra uma nova](https://github.com/DiegoNogueiraDev/context-guide/issues/new).
   - Inclua um título e descrição clara
   - Descreva os passos para reproduzir o bug
   - Descreva o comportamento esperado e o que aconteceu de fato
   - Inclua detalhes sobre seu ambiente (sistema operacional, versão do Python, etc.)

### Sugerindo Melhorias

Se você tem uma ideia para melhorar o Context Guide:

1. Verifique se a melhoria já foi sugerida nas [Issues](https://github.com/DiegoNogueiraDev/context-guide/issues).
2. Abra uma nova issue descrevendo a melhoria sugerida.
   - Explique por que essa melhoria seria útil
   - Considere como ela poderia ser implementada

### Enviando Pull Requests

1. Faça um fork do repositório
2. Crie uma branch para sua feature ou correção: `git checkout -b feature/nome-da-feature` ou `git checkout -b fix/nome-do-bug`
3. Implemente suas mudanças
4. Adicione ou atualize testes conforme necessário
5. Execute `pytest` para garantir que os testes passem
6. Verifique a formatação do código com `black` e `flake8`
7. Commit suas mudanças: `git commit -m 'Descrição clara da mudança'` 
8. Push para sua branch: `git push origin feature/nome-da-feature`
9. Abra um Pull Request

## Ambiente de Desenvolvimento

### Configuração

```bash
# Clone o repositório
git clone https://github.com/DiegoNogueiraDev/context-guide.git
cd context-guide

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate     # Windows

# Instale as dependências de desenvolvimento
pip install -e ".[dev]"
```

### Executando Testes

```bash
# Executar todos os testes
pytest

# Executar com cobertura
pytest --cov=context_guide tests/

# Executar com relatório HTML de cobertura
pytest --cov=context_guide --cov-report=html tests/
```

### Verificação de Estilo

```bash
# Formatar código com black
black context_guide/ tests/

# Verificar problemas com flake8
flake8 context_guide/ tests/
```

## Estrutura do Código

O Context Guide segue esta estrutura:

```
context-guide/
├── context_guide/         # Código fonte principal
│   ├── __init__.py        # Inicialização do pacote
│   ├── cli.py             # Interface de linha de comando
│   ├── context.py         # Gerenciamento de contexto (RAG)
│   ├── watcher.py         # Monitoramento de alterações
│   ├── prompt_generator.py # Geração de prompts
│   └── project_templates.py # Templates de documentação
├── tests/                 # Testes unitários
├── docs/                  # Documentação
├── setup.py               # Configuração de instalação
└── pyproject.toml         # Metadados do projeto
```

## Diretrizes de Código

- Use docstrings no formato Google Python para documentar funções e classes
- Mantenha a cobertura de testes acima de 80%
- Siga a PEP 8 para convenções de estilo
- Use anotações de tipo (type hints) onde possível

## Processo de Lançamento

- A versão segue o padrão Semântico: MAJOR.MINOR.PATCH
- Atualize a versão em `context_guide/__init__.py` e `pyproject.toml`
- Crie uma tag para o lançamento: `git tag -a v0.1.0 -m "Lançamento v0.1.0"`

## Licença

Ao contribuir para o Context Guide, você concorda que suas contribuições serão licenciadas sob a [Licença MIT](LICENSE) que cobre o projeto. 