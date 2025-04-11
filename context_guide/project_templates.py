"""
Módulo que contém templates de documentação para diferentes tipos de projetos.
"""

# Templates básicos de projeto
OVERVIEW_TEMPLATE = """# Visão Geral do Projeto

## Propósito
[Descreva aqui o propósito principal do seu projeto]

## Tecnologias Principais
- Frontend: [Framework principal, ex: React, Vue, Angular]
- Backend: [Framework principal, ex: Node.js, Django, Rails]
- Database: [Tipo de banco de dados, ex: PostgreSQL, MongoDB]
- Outras ferramentas: [Outras ferramentas importantes]

## Status do Projeto
- Data de início: [DD/MM/AAAA]
- Fase atual: [Planejamento/MVP/Beta/Produção]
- Versão atual: [x.y.z]

## Estrutura Organizacional
- Equipe responsável: [Nome da equipe]
- Principais stakeholders: [Lista de stakeholders]
"""

ARCHITECTURE_TEMPLATE = """# Arquitetura do Projeto

## Visão Geral da Arquitetura
[Descreva aqui a arquitetura geral do sistema, pode incluir um diagrama]

## Frontend
- **Framework**: [Nome e versão]
- **Gerenciamento de Estado**: [Redux, Context API, MobX, etc.]
- **Roteamento**: [React Router, Vue Router, etc.]
- **Estilização**: [Tailwind, Styled Components, SASS, etc.]
- **Componentes**: [Bibliotecas de componentes utilizadas]

## Backend
- **Framework/Linguagem**: [Nome e versão]
- **API**: [REST, GraphQL, gRPC]
- **Autenticação**: [JWT, OAuth, etc.]
- **Validação**: [Bibliotecas de validação]
- **Middleware**: [Middleware importantes]

## Banco de Dados
- **Tipo**: [Relacional, NoSQL, NewSQL]
- **Sistema**: [PostgreSQL, MongoDB, MySQL, etc.]
- **ORM/ODM**: [Mongoose, Sequelize, Prisma, etc.]
- **Estratégia de Migração**: [Como as migrações são gerenciadas]

## Infraestrutura
- **Hospedagem**: [AWS, GCP, Azure, on-premise]
- **Deploy**: [CI/CD, ferramentas utilizadas]
- **Monitoramento**: [Ferramentas de observabilidade]
- **Cache**: [Estratégia de cache, Redis, Memcached]

## Segurança
- **Autenticação de Usuários**: [Estratégia]
- **Autorização**: [RBAC, ABAC, etc.]
- **Proteção de Dados**: [Estratégias de proteção]
- **Conformidade**: [Padrões de conformidade: GDPR, LGPD, etc.]

## Escalabilidade
- **Estratégia de Escala Horizontal**: [Abordagem]
- **Balanceamento de Carga**: [Ferramentas]
- **Otimização de Performance**: [Estratégias]
"""

COMPONENTS_TEMPLATE = """# Componentes do Projeto

## Componentes de UI/Frontend
[Liste aqui os principais componentes da interface de usuário e suas propriedades]

- **ComponenteA** (`prop1: tipo, prop2: tipo`)
  - Descrição: [Descrição do componente]
  - Localização: [Caminho relativo no projeto]
  - Dependências: [Outros componentes que este utiliza]

- **ComponenteB** (`prop1: tipo, prop2: tipo`)
  - Descrição: [Descrição do componente]
  - Localização: [Caminho relativo no projeto]
  - Dependências: [Outros componentes que este utiliza]

## Componentes de Backend/Serviços
[Liste aqui os principais serviços/componentes do backend]

- **ServiçoA**
  - Responsabilidade: [Descrição da responsabilidade]
  - Endpoints/Métodos: [Lista de endpoints ou métodos principais]
  - Dependências: [Outros serviços que este utiliza]

- **ServiçoB**
  - Responsabilidade: [Descrição da responsabilidade]
  - Endpoints/Métodos: [Lista de endpoints ou métodos principais]
  - Dependências: [Outros serviços que este utiliza]

## Modelos de Dados
[Liste aqui os principais modelos de dados/entidades]

- **ModeloA**
  - Atributos: [Lista de atributos principais]
  - Relacionamentos: [Relacionamentos com outros modelos]
  - Validações: [Regras de validação]

- **ModeloB**
  - Atributos: [Lista de atributos principais]
  - Relacionamentos: [Relacionamentos com outros modelos]
  - Validações: [Regras de validação]
"""

FEATURES_TEMPLATE = """# Funcionalidades do Projeto

## Funcionalidades Principais
[Liste aqui as principais funcionalidades do sistema]

### Funcionalidade A
- Descrição: [Descrição detalhada]
- Status: [Planejada/Em desenvolvimento/Concluída/Testada]
- Prioridade: [Alta/Média/Baixa]
- Dependências: [Outras funcionalidades dependentes]
- Critérios de aceitação:
  - [Critério 1]
  - [Critério 2]

### Funcionalidade B
- Descrição: [Descrição detalhada]
- Status: [Planejada/Em desenvolvimento/Concluída/Testada]
- Prioridade: [Alta/Média/Baixa]
- Dependências: [Outras funcionalidades dependentes]
- Critérios de aceitação:
  - [Critério 1]
  - [Critério 2]

## Roadmap de Funcionalidades
[Timeline e roadmap de implementação das funcionalidades]

- Fase 1 (MVP):
  - [Funcionalidade X]
  - [Funcionalidade Y]
  
- Fase 2:
  - [Funcionalidade Z]
  - [Funcionalidade W]
"""

# Templates para acompanhamento de desenvolvimento

TASKS_TEMPLATE = """# Tarefas e Progresso do Projeto

## Visão Geral do Progresso
- Progresso total estimado: [x%]
- Data de última atualização: [DD/MM/AAAA]

## Tarefas Atuais

### Sprint/Ciclo Atual: [Nome/Número]
- Período: [DD/MM/AAAA - DD/MM/AAAA]
- Objetivo: [Objetivo principal desta sprint/ciclo]

| ID | Tarefa | Responsável | Status | Prioridade | Estimativa | Observações |
|----|--------|-------------|--------|------------|------------|-------------|
| T1 | [Descrição] | [Nome] | [Pendente/Em andamento/Concluída/Bloqueada] | [Alta/Média/Baixa] | [xh] | [Observações] |
| T2 | [Descrição] | [Nome] | [Pendente/Em andamento/Concluída/Bloqueada] | [Alta/Média/Baixa] | [xh] | [Observações] |

## Tarefas Concluídas

### Sprint/Ciclo Anterior: [Nome/Número]
- Período: [DD/MM/AAAA - DD/MM/AAAA]
- Objetivo alcançado: [Sim/Parcialmente/Não]

| ID | Tarefa | Responsável | Concluída em | Tempo Real | Observações |
|----|--------|-------------|--------------|------------|-------------|
| T1 | [Descrição] | [Nome] | [DD/MM/AAAA] | [xh] | [Observações] |
| T2 | [Descrição] | [Nome] | [DD/MM/AAAA] | [xh] | [Observações] |

## Bloqueios e Impedimentos

| ID | Descrição | Afeta | Responsável | Reportado em | Status | Plano de Ação |
|----|-----------|-------|-------------|--------------|--------|---------------|
| B1 | [Descrição] | [Tarefas afetadas] | [Nome] | [DD/MM/AAAA] | [Aberto/Resolvido] | [Plano] |
"""

MODULES_STATUS_TEMPLATE = """# Status dos Módulos

## Visão Geral
- Total de módulos: [Número]
- Módulos funcionais: [Número/Porcentagem]
- Módulos com problemas: [Número/Porcentagem]
- Data de última verificação: [DD/MM/AAAA]

## Status por Módulo

### Frontend

| Módulo | Versão | Status | Cobertura de Testes | Problemas Conhecidos | Última Atualização |
|--------|--------|--------|---------------------|----------------------|-------------------|
| [Nome] | [x.y.z] | [Funcional/Instável/Crítico] | [x%] | [Descrição ou "Nenhum"] | [DD/MM/AAAA] |
| [Nome] | [x.y.z] | [Funcional/Instável/Crítico] | [x%] | [Descrição ou "Nenhum"] | [DD/MM/AAAA] |

### Backend

| Módulo | Versão | Status | Cobertura de Testes | Problemas Conhecidos | Última Atualização |
|--------|--------|--------|---------------------|----------------------|-------------------|
| [Nome] | [x.y.z] | [Funcional/Instável/Crítico] | [x%] | [Descrição ou "Nenhum"] | [DD/MM/AAAA] |
| [Nome] | [x.y.z] | [Funcional/Instável/Crítico] | [x%] | [Descrição ou "Nenhum"] | [DD/MM/AAAA] |

### Infraestrutura/DevOps

| Módulo | Versão | Status | Monitorado | Problemas Conhecidos | Última Atualização |
|--------|--------|--------|------------|----------------------|-------------------|
| [Nome] | [x.y.z] | [Funcional/Instável/Crítico] | [Sim/Não] | [Descrição ou "Nenhum"] | [DD/MM/AAAA] |
| [Nome] | [x.y.z] | [Funcional/Instável/Crítico] | [Sim/Não] | [Descrição ou "Nenhum"] | [DD/MM/AAAA] |

## Dependências Externas

| Dependência | Versão | Status | Alternativas | Observações |
|-------------|--------|--------|--------------|-------------|
| [Nome] | [x.y.z] | [Estável/Problema] | [Alternativas] | [Observações] |
| [Nome] | [x.y.z] | [Estável/Problema] | [Alternativas] | [Observações] |
"""

TESTING_STATUS_TEMPLATE = """# Status de Testes

## Sumário de Testes
- Cobertura total: [x%]
- Total de testes: [Número]
- Testes passando: [Número/Porcentagem]
- Testes falhando: [Número/Porcentagem]
- Data de última execução: [DD/MM/AAAA]

## Status por Grupo de Testes

### Testes Unitários

| Grupo | Total | Passando | Falhando | Ignorados | Duração | Última Execução |
|-------|-------|----------|----------|-----------|---------|-----------------|
| [Nome] | [Num] | [Num] | [Num] | [Num] | [Tempo] | [DD/MM/AAAA] |
| [Nome] | [Num] | [Num] | [Num] | [Num] | [Tempo] | [DD/MM/AAAA] |

### Testes de Integração

| Grupo | Total | Passando | Falhando | Ignorados | Duração | Última Execução |
|-------|-------|----------|----------|-----------|---------|-----------------|
| [Nome] | [Num] | [Num] | [Num] | [Num] | [Tempo] | [DD/MM/AAAA] |
| [Nome] | [Num] | [Num] | [Num] | [Num] | [Tempo] | [DD/MM/AAAA] |

### Testes End-to-End

| Grupo | Total | Passando | Falhando | Ignorados | Duração | Última Execução |
|-------|-------|----------|----------|-----------|---------|-----------------|
| [Nome] | [Num] | [Num] | [Num] | [Num] | [Tempo] | [DD/MM/AAAA] |
| [Nome] | [Num] | [Num] | [Num] | [Num] | [Tempo] | [DD/MM/AAAA] |

## Falhas Recorrentes

| Teste | Módulo | Frequência | Desde | Possível Causa | Status |
|-------|--------|------------|-------|----------------|--------|
| [Nome] | [Módulo] | [X de Y execuções] | [DD/MM/AAAA] | [Descrição] | [Investigando/Corrigido] |
| [Nome] | [Módulo] | [X de Y execuções] | [DD/MM/AAAA] | [Descrição] | [Investigando/Corrigido] |
"""

API_DOCS_TEMPLATE = """# Documentação da API

## Visão Geral
- Base URL: [URL base da API]
- Versão atual: [x.y.z]
- Formato: [REST/GraphQL/gRPC]
- Autenticação: [Método de autenticação]

## Endpoints

### Grupo: [Nome do Grupo/Recurso]

#### `[MÉTODO] /[caminho]`

- **Descrição**: [Descrição do endpoint]
- **Autenticação**: [Requerida/Opcional/Não requerida]
- **Parâmetros de URL**:
  - `[nome]`: [tipo] - [descrição] - [obrigatório/opcional]
  
- **Corpo da Requisição** (se aplicável):
```json
{
  "campo1": "valor1",
  "campo2": "valor2"
}
```

- **Resposta de Sucesso**:
  - Código: [código HTTP]
  - Conteúdo:
```json
{
  "campo1": "valor1",
  "campo2": "valor2"
}
```

- **Respostas de Erro**:
  - Código: [código HTTP]
  - Conteúdo:
```json
{
  "erro": "mensagem de erro"
}
```

- **Notas**:
  - [Qualquer informação adicional]

#### `[MÉTODO] /[outro-caminho]`
...

## Modelos de Dados

### [Nome do Modelo]

| Campo | Tipo | Descrição | Obrigatório |
|-------|------|-----------|-------------|
| [nome] | [tipo] | [descrição] | [Sim/Não] |
| [nome] | [tipo] | [descrição] | [Sim/Não] |

## Autenticação e Autorização

### Obtenção de Token

- **Endpoint**: `POST /auth/token`
- **Corpo da Requisição**:
```json
{
  "username": "usuario",
  "password": "senha"
}
```

- **Resposta**:
```json
{
  "token": "eyJhbGciOiJ...",
  "expira_em": "timestamp"
}
```

### Utilização de Token

Inclua o token no cabeçalho HTTP `Authorization` de cada requisição:

```
Authorization: Bearer eyJhbGciOiJ...
```
"""

BEST_PRACTICES_TEMPLATE = """# Melhores Práticas e Padrões do Projeto

## Padrões de Código

### Estilo de Código
- **Frontend**:
  - [Convenções de nomenclatura]
  - [Formatação]
  - [Linter utilizado]
  
- **Backend**:
  - [Convenções de nomenclatura]
  - [Formatação]
  - [Linter utilizado]

### Padrões de Commit
- Formato de mensagem: [ex: "feat(component): add new button component"]
- Branches: [Convenção de nomes de branches]
- Pull Requests: [Critérios para aprovação]

## Arquitetura e Design

### Princípios Arquiteturais
- [Princípios que guiam a arquitetura do projeto]
- [Decisões arquiteturais importantes]

### Padrões de Design
- Frontend: [Padrões como Atomic Design, Container/Presentational, etc.]
- Backend: [Padrões como Repository, Service Layer, etc.]

## Segurança

### Diretrizes de Segurança
- [Práticas de autenticação]
- [Validação de entrada]
- [Proteção contra vulnerabilidades comuns]

### Gestão de Dados Sensíveis
- [Como lidar com dados do usuário]
- [Criptografia]
- [Conformidade com regulamentos]

## Testes

### Estratégia de Testes
- [Abordagem geral para testes]
- [Tipos de testes implementados]
- [Cobertura mínima exigida]

### Práticas de Testes
- [Como escrever testes úteis]
- [Nomenclatura de testes]
- [Mocking e fixtures]

## Performance

### Otimização Frontend
- [Boas práticas para componentes]
- [Carregamento e renderização]
- [Gestão de estado]

### Otimização Backend
- [Consultas ao banco de dados]
- [Caching]
- [Concorrência]

## DevOps e Infraestrutura

### CI/CD
- [Pipeline de integração contínua]
- [Processo de deploy]
- [Ambientes (dev, staging, prod)]

### Monitoramento e Logs
- [O que monitorar]
- [Formato de logs]
- [Alerta e resolução de problemas]
"""

TOOLS_ENVIRONMENT_TEMPLATE = """# Ferramentas e Ambiente de Desenvolvimento

## Ambiente de Desenvolvimento

### Requisitos
- Sistema Operacional: [Compatível com Windows/macOS/Linux]
- Node.js: [versão]
- Python: [versão]
- Banco de Dados: [PostgreSQL/MongoDB/etc. e versão]
- Outras dependências: [Docker, etc.]

### Setup Inicial
1. Clone o repositório:
```bash
git clone [url-do-repositorio]
cd [nome-do-projeto]
```

2. Instale as dependências:
```bash
# Frontend
cd frontend
npm install

# Backend
cd backend
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

4. Inicie o ambiente de desenvolvimento:
```bash
# Frontend
npm run dev

# Backend
python manage.py runserver  # ou comando equivalente
```

## Ferramentas Recomendadas

### IDE e Editores
- [VSCode/IntelliJ/etc.]
- Extensões recomendadas:
  - [Lista de extensões úteis]

### Ferramentas de Desenvolvimento
- Gerenciamento de Estado: [Redux DevTools, etc.]
- API Testing: [Postman, Insomnia, etc.]
- Database: [GUI recomendado]

### Ferramentas de Qualidade
- Linting: [ESLint, Prettier, etc.]
- Testing: [Jest, Cypress, etc.]
- Coverage: [Ferramenta de cobertura]

## Ambientes

### Desenvolvimento
- URL: [url-dev]
- Acesso: [Como acessar]
- Limitações: [Qualquer limitação do ambiente]

### Staging/QA
- URL: [url-staging]
- Atualização: [Frequência e método]
- Dados: [Origem dos dados]

### Produção
- URL: [url-prod]
- Deploy: [Processo de deploy]
- Monitoramento: [Ferramentas]

## Processos

### Desenvolvimento de Features
1. [Processo para criar uma nova feature]
2. [Code review]
3. [Testes]
4. [Deploy]

### Resolução de Bugs
1. [Processo para reportar bugs]
2. [Priorização]
3. [Fixar e verificar]
"""

DEPLOYMENT_TEMPLATE = """# Guia de Deployment

## Estratégia de Deployment
- Abordagem: [CI/CD, Deploy Manual, etc.]
- Frequência: [Contínuo, Agendado, Por Demanda]
- Ambientes: [Desenvolvimento, Staging, Produção]

## Requisitos de Infraestrutura

### Frontend
- Servidor Web: [Nginx, Apache, etc.]
- Hospedagem: [Vercel, Netlify, AWS S3, etc.]
- Recursos recomendados: [CPU, RAM, etc.]

### Backend
- Servidor: [Node.js, Django, etc.]
- Hospedagem: [AWS EC2, Heroku, etc.]
- Recursos recomendados: [CPU, RAM, etc.]

### Banco de Dados
- Tipo: [PostgreSQL, MongoDB, etc.]
- Hospedagem: [RDS, Atlas, etc.]
- Recursos recomendados: [CPU, RAM, Storage]

### Serviços Adicionais
- Cache: [Redis, Memcached, etc.]
- CDN: [Cloudflare, Akamai, etc.]
- Storage: [S3, Google Cloud Storage, etc.]

## Procedimento de Deploy

### Preparação
1. [Verificações pré-deploy]
2. [Backup de dados]
3. [Comunicação com stakeholders]

### Deploy Frontend
1. ```bash
   # Comando para build
   npm run build
   
   # Comando para deploy
   [comando de deploy]
   ```
2. [Etapas de verificação pós-deploy]
3. [Rollback se necessário]

### Deploy Backend
1. ```bash
   # Comando para preparar o ambiente
   [comandos de preparação]
   
   # Comando para deploy
   [comando de deploy]
   ```
2. [Migrações de banco de dados]
3. [Etapas de verificação pós-deploy]
4. [Rollback se necessário]

## Monitoramento Pós-Deploy

### Métricas a Observar
- Performance: [Tempo de resposta, latência, etc.]
- Recursos: [CPU, memória, disco, etc.]
- Negócio: [Conversões, usuários ativos, etc.]

### Resolução de Problemas
- Logs: [Onde encontrar e como interpretar]
- Alertas: [Sistema de alerta configurado]
- Contatos: [Quem contatar em caso de problemas]

## Procedimentos de Rollback

### Quando Fazer Rollback
- [Critérios para decisão de rollback]

### Como Fazer Rollback
1. ```bash
   # Comandos para rollback frontend
   [comandos]
   ```

2. ```bash
   # Comandos para rollback backend
   [comandos]
   ```

3. ```bash
   # Comandos para rollback de banco de dados
   [comandos]
   ```
"""

# Templates específicos para diferentes tipos de aplicações

WEB_APP_TEMPLATE = """# Arquitetura de Aplicação Web

## Frontend

### Framework e Bibliotecas
- Framework Principal: [React/Vue/Angular/Svelte]
- Gerenciamento de Estado: [Redux/Vuex/Context API/Recoil]
- Roteamento: [React Router/Vue Router]
- UI/Componentes: [Material UI/Chakra UI/Tailwind]
- Formulários: [Formik/React Hook Form/Vuelidate]
- Validação: [Yup/Zod/Joi]

### Estrutura de Diretórios Recomendada
```
src/
├── assets/          # Imagens, fontes, etc.
├── components/      # Componentes reutilizáveis
│   ├── common/      # Componentes genéricos (Button, Input, etc.)
│   ├── layout/      # Componentes de layout (Header, Footer, etc.)
│   └── feature/     # Componentes específicos de features
├── hooks/           # Hooks personalizados
├── pages/           # Componentes de página
├── services/        # Serviços e APIs
├── store/           # Gerenciamento de estado global
├── styles/          # Estilos globais e temas
├── utils/           # Utilitários e helpers
└── App.js           # Componente principal
```

### Padrões Recomendados
- Componentes: [Functional Components, Styled Components, etc.]
- Estado: [Padrões para gerenciar estado]
- Renderização: [Otimizações, Code Splitting, Lazy Loading]
- Comunicação com Backend: [REST, GraphQL, Websockets]

## Backend

### Framework e Bibliotecas
- Framework Principal: [Express/Django/Rails/Spring]
- ORM/Acesso a Dados: [Sequelize/Prisma/SQLAlchemy]
- Autenticação: [JWT/OAuth/Passport]
- Validação: [Joi/Yup/Marshmallow]
- Documentação: [Swagger/OpenAPI]

### Estrutura de Diretórios Recomendada
```
src/
├── config/          # Configurações
├── controllers/     # Controladores/handlers
├── middleware/      # Middleware
├── models/          # Modelos de dados
├── routes/          # Definições de rotas
├── services/        # Lógica de negócio
├── utils/           # Utilitários
└── app.js           # Arquivo principal
```

### Padrões Recomendados
- Arquitetura: [MVC, Clean Architecture, etc.]
- API: [RESTful, GraphQL]
- Segurança: [Validação, Sanitização, Autenticação]
- Performance: [Caching, Otimização de Consultas]

## Banco de Dados

### Tipo Recomendado
- Relacional: [PostgreSQL, MySQL]
- NoSQL: [MongoDB, Firebase]
- Híbrido: [Estratégia]

### Design de Esquema
- [Recomendações para modelagem]
- [Estratégia de migrations]
- [Indexação e otimização]

## DevOps

### Desenvolvimento
- Ambiente Local: [Docker, docker-compose]
- Dependências: [Gerenciamento]

### CI/CD
- Pipelines: [GitHub Actions, GitLab CI, Jenkins]
- Testes: [Unitários, Integração, E2E]
- Deploy: [Estratégia de deployment]

### Infraestrutura
- Hospedagem: [AWS, GCP, Azure, Vercel, Netlify]
- Escala: [Estratégias de escalabilidade]
- Monitoramento: [Ferramentas e métricas]
"""

MOBILE_APP_TEMPLATE = """# Arquitetura de Aplicação Mobile

## Abordagem de Desenvolvimento

### Opções Disponíveis
- Nativa: [iOS (Swift/Objective-C), Android (Kotlin/Java)]
- Cross-Platform: [React Native, Flutter, Xamarin]
- Híbrida: [Ionic, Capacitor]

### Recomendação para o Projeto
- [Abordagem escolhida e justificativa]
- [Considerações sobre performance, UI/UX, e recursos nativos]

## Estrutura da Aplicação

### Arquitetura
- [Clean Architecture, MVVM, MVC, Redux]
- [Fluxo de dados]
- [Separação de responsabilidades]

### Estrutura de Diretórios Recomendada

#### React Native
```
src/
├── assets/          # Imagens, fontes, etc.
├── components/      # Componentes reutilizáveis
├── navigation/      # Configuração de navegação
├── screens/         # Telas da aplicação
├── services/        # Serviços e APIs
├── store/           # Gerenciamento de estado (Redux, etc.)
├── styles/          # Estilos e temas
└── utils/           # Utilitários
```

#### Flutter
```
lib/
├── assets/          # Imagens, fontes, etc.
├── models/          # Modelos de dados
├── providers/       # Provedores de estado
├── screens/         # Telas da aplicação
├── services/        # Serviços e APIs
├── widgets/         # Widgets personalizados
└── utils/           # Utilitários
```

### Componentes Principais
- [Componentes/widgets comuns]
- [Padrões de UI a seguir]
- [Navegação e gerenciamento de rotas]

## Funcionalidades Nativas

### Acesso a Hardware
- [Câmera, GPS, Sensores]
- [Permissões e melhores práticas]

### Armazenamento
- [Local Storage, Secure Storage]
- [Persistência de dados]
- [Sincronização com backend]

### Notificações
- [Push Notifications]
- [Notificações locais]
- [Estratégias de engajamento]

## Integrações

### APIs e Backend
- [Comunicação com backend]
- [Autenticação e segurança]
- [Manipulação de erros e casos offline]

### Serviços de Terceiros
- [Analytics, Crash Reporting]
- [Autenticação social]
- [Outros serviços relevantes]

## Publicação e Distribuição

### App Store (iOS)
- [Requisitos]
- [Processo de revisão]
- [Certificados e provisioning]

### Google Play (Android)
- [Requisitos]
- [Processo de publicação]
- [Assinatura da aplicação]

### Testes e Qualidade
- [Estratégia de testes]
- [Automação de testes]
- [Testes com usuários reais]

## Atualizações e Manutenção

### Atualizações OTA (Over The Air)
- [Estratégias para atualizações de código sem republicação]
- [Gerenciamento de versões]

### Monitoramento
- [Métricas importantes]
- [Ferramentas de monitoramento]
- [Resposta a problemas em produção]
"""

DESKTOP_APP_TEMPLATE = """# Arquitetura de Aplicação Desktop

## Abordagem de Desenvolvimento

### Opções Disponíveis
- Electron: [JavaScript/TypeScript + HTML/CSS]
- Qt: [C++, Python]
- .NET: [C#, XAML]
- Java: [JavaFX, Swing]
- Tauri: [Rust + Web Technologies]

### Recomendação para o Projeto
- [Abordagem escolhida e justificativa]
- [Considerações sobre performance, UI/UX, e integração com o sistema]

## Estrutura da Aplicação

### Arquitetura
- [Arquitetura de camadas]
- [Processo principal vs. renderização (no caso de Electron/Tauri)]
- [Padrões arquiteturais: MVC, MVVM, etc.]

### Estrutura de Diretórios Recomendada

#### Electron
```
src/
├── main/           # Processo principal
│   ├── main.js     # Ponto de entrada
│   ├── ipc/        # Comunicação entre processos
│   └── services/   # Serviços do sistema
├── renderer/       # Processo de renderização (UI)
│   ├── components/ # Componentes de UI
│   ├── pages/      # Páginas/telas
│   ├── store/      # Estado (Redux, etc.)
│   └── utils/      # Utilitários
├── common/         # Código compartilhado
└── assets/         # Recursos estáticos
```

#### .NET WPF/MAUI
```
src/
├── Models/         # Modelos de dados
├── ViewModels/     # View models (MVVM)
├── Views/          # Interface de usuário
├── Services/       # Serviços e lógica de negócio
├── Helpers/        # Classes auxiliares
└── Resources/      # Recursos estáticos
```

### Componentes Principais
- [Componentes/controles comuns]
- [Padrões de UI a seguir]
- [Navegação entre telas/janelas]

## Funcionalidades Específicas

### Integração com Sistema Operacional
- [Sistema de arquivos]
- [Serviços do sistema]
- [Notificações e barra de status]

### Instalação e Atualização
- [Processo de instalação]
- [Atualizações automáticas]
- [Persistência de configurações]

### Comunicação com Hardware
- [Dispositivos conectados]
- [Periféricos]
- [Recursos específicos de hardware]

## Empacotamento e Distribuição

### Windows
- [Instaladores: MSI, NSIS, etc.]
- [Windows Store (se aplicável)]
- [Certificados e assinatura]

### macOS
- [DMG, PKG]
- [Mac App Store (se aplicável)]
- [Notarização e sandboxing]

### Linux
- [AppImage, Snap, Flatpak, DEB, RPM]
- [Gestão de dependências]
- [Integração com desktop environments]

## Segurança

### Proteção de Dados
- [Criptografia]
- [Armazenamento seguro de credenciais]
- [Prevenção contra vazamentos de memória]

### Comunicação Segura
- [HTTPS, WSS]
- [Certificados cliente/servidor]
- [Validação de conexões]

## Performance e Recursos

### Otimização
- [Uso de memória]
- [Inicialização rápida]
- [Processamento em background]

### Diagnóstico
- [Logging]
- [Telemetria e analytics]
- [Relatórios de erros]
"""

# Coleção de templates por tipo de projeto
PROJECT_TEMPLATES = {
    "basic": {
        "overview.md": OVERVIEW_TEMPLATE,
        "architecture.md": ARCHITECTURE_TEMPLATE,
        "components.md": COMPONENTS_TEMPLATE,
        "features.md": FEATURES_TEMPLATE,
    },
    "tracking": {
        "tasks.md": TASKS_TEMPLATE,
        "modules-status.md": MODULES_STATUS_TEMPLATE,
        "testing-status.md": TESTING_STATUS_TEMPLATE
    },
    "development": {
        "api-docs.md": API_DOCS_TEMPLATE,
        "best-practices.md": BEST_PRACTICES_TEMPLATE,
        "tools-environment.md": TOOLS_ENVIRONMENT_TEMPLATE,
        "deployment.md": DEPLOYMENT_TEMPLATE
    },
    "app_types": {
        "web-app.md": WEB_APP_TEMPLATE,
        "mobile-app.md": MOBILE_APP_TEMPLATE,
        "desktop-app.md": DESKTOP_APP_TEMPLATE
    }
} 