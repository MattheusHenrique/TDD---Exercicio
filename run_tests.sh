#!/bin/bash

echo "Snake Game - Ambiente de Testes"

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


export SNAKE_TESTING=1
export PYTHONPATH="$(pwd)"

echo "Executando testes com pytest..."
pytest -q