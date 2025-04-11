# Componentes da UI

## Componentes de Layout
- **Header** (`title: string, showLogo: boolean = true`) - Cabeçalho principal com logo e título da página
- **Footer** (`showLinks: boolean = true`) - Rodapé com links de contato e redes sociais
- **Sidebar** (`items: MenuItem[], activeItem: string`) - Barra lateral de navegação

## Componentes de Autenticação
- **LoginForm** (`onSuccess: function`) - Formulário de login com email e senha
- **SignupForm** (`onSuccess: function`) - Formulário de cadastro de novos usuários
- **ForgotPasswordForm** (`onSuccess: function`) - Formulário para recuperação de senha

## Componentes do Onboarding
- **OnboardingContainer** (`currentStep: number, totalSteps: number`) - Container principal do onboarding
- **StepIndicator** (`currentStep: number, totalSteps: number`) - Indicador visual de progresso
- **CardOnboarding** (`step: number, content: string, image: string`) - Card para cada etapa do onboarding
- **ActionButton** (`label: string, onClick: function, variant: 'primary' | 'secondary'`) - Botão de ação customizável

## Componentes de Gamificação
- **ProgressBar** (`progress: number, total: number`) - Barra de progresso para atividades
- **Badge** (`type: string, label: string, achieved: boolean`) - Distintivo para conquistas
- **ScoreCounter** (`score: number, animate: boolean`) - Contador de pontos com animação
- **LevelIndicator** (`level: number, progress: number`) - Indicador do nível atual do usuário

## Componentes de Exercícios
- **QuizCard** (`question: string, options: string[], onAnswer: function`) - Card para exercícios de quiz
- **AudioExercise** (`audioUrl: string, transcript: string`) - Componente para exercícios de áudio
- **TextInput** (`placeholder: string, value: string, onChange: function`) - Input de texto para exercícios de escrita
- **DragDropExercise** (`items: string[], correctOrder: number[]`) - Exercício de arrastar e soltar