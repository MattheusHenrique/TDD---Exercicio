# Snake Game

Jogo Snake implementado em Python com interface de terminal, desenvolvido usando TDD.

## Como executar

### Instalação

```bash
git clone <url-do-repositorio>
cd TDD---Exercicio
pip install -r requirements.txt
```

### Jogar

```bash
python3 snake-screen.py
```

### Testes

```bash
./run_tests.sh
```

## Controles

- **WASD** - Mover a cobra
- **ESC** - Sair

## Regras do jogo

- A cobra cresce ao comer frutas (🍎)
- Game over ao colidir com o próprio corpo
- A cobra atravessa as bordas (wrap-around)
- A cada 10 crescimentos, aparece uma fruta adicional no campo

## Estrutura

- `snake.py` - Lógica da cobra
- `snake-screen.py` - Interface e loop do jogo
- `tests/test_snake.py` - Testes unitários
- `run_tests.sh` - Script para executar testes
- `run.sh` - Script para executar o jogo

## Dependências

- Python 3.12+
- pytest
- pynput (captura de teclas)