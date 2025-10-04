#!/bin/bash

echo "Snake Game - Setup e Execução"
echo "=============================="

# Verificar se o venv existe
if [ ! -d "venv" ]; then
    echo "Criando ambiente virtual..."
    python3 -m venv venv
fi

# Ativar o venv
echo "Ativando ambiente virtual..."
source venv/bin/activate

# Instalar dependências
echo "Instalando dependências..."
pip install -r requirements.txt

# Executar o jogo
echo "Executando o jogo Snake..."
echo "Use WASD para mover, ESC para sair"
echo "=============================="
python3 snake-screen.py