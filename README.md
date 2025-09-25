# Snake Game 🐍

Um jogo Snake simples implementado em Python com interface de terminal, desenvolvido seguindo princípios de TDD (Test-Driven Development).

## 📋 Pré-requisitos

- Python 3.12 ou superior
- pip (gerenciador de pacotes do Python)
- Docker (opcional, para execução em container)

## 🚀 Instalação e Execução

### Opção 1: Execução Local

1. **Clone o repositório:**

   ```bash
   git clone <url-do-repositorio>
   cd TDD---Exercicio
   ```

2. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o jogo:**

   ```bash
   python snake-screen.py
   ```

### Opção 2: Execução com Docker

1. **Clone o repositório:**

   ```bash
   git clone <url-do-repositorio>
   cd TDD---Exercicio
   ```

2. **Execute com Docker:**

   ```bash
   docker run -it --rm -v $(pwd):/app -w /app python:3.12-slim bash -c "pip install -r requirements.txt && python snake-screen.py"
   ```

   **Para Windows (PowerShell):**

   ```powershell
   docker run -it --rm -v ${PWD}:/app -w /app python:3.12-slim bash -c "pip install -r requirements.txt && python snake-screen.py"
   ```

### Opção 3: Docker Compose (Recomendado)

1. **Crie um arquivo `docker-compose.yml`:**

   ```yaml
   version: '3.8'
   services:
     snake-game:
       image: python:3.12-slim
       working_dir: /app
       volumes:
         - .:/app
       command: bash -c "pip install -r requirements.txt && python snake-screen.py"
       stdin_open: true
       tty: true
   ```

2. **Execute o jogo:**

   ```bash
   docker-compose up
   ```

## 🎮 Como Jogar

- **W** - Mover para cima
- **A** - Mover para esquerda  
- **S** - Mover para baixo
- **D** - Mover para direita
- **ESC** - Sair do jogo

## 🧪 Executando os Testes

Para executar os testes do projeto:

```bash
# Localmente
pytest

# Com Docker
docker run -it --rm -v $(pwd):/app -w /app python:3.12-slim bash -c "pip install -r requirements.txt && pytest"
```

## 📁 Estrutura do Projeto

```text
TDD---Exercicio/
├── snake.py              # Módulo principal (em desenvolvimento)
├── snake-screen.py       # Interface de terminal e loop do jogo
├── requirements.txt      # Dependências do projeto
├── tests/
│   └── test_snake.py     # Testes unitários
└── README.md            # Este arquivo
```

## 🔧 Dependências

- **python**: 3.12
- **pytest**: 8.3.4 (para testes)
- **python-coverage**: 7.3.2 (para cobertura de testes)
- **keyboard**: Para captura de teclas (instalada via pip)