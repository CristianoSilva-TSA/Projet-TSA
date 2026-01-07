#!/bin/bash

# Configurações
read -p "Introduza o IP do Servidor (ex: 127.0.0.1): " SERVER_IP
PORT=5000

echo "--- Bem-vindo ao Rock, Paper, Scissors Online ---"
echo "Opções: pedra, papel, tesoura"
read -p "Qual a sua jogada? " JOGADA

# Validação simples
JOGADA=$(echo $JOGADA | tr '[:upper:]' '[:lower:]')

if [[ "$JOGADA" == "pedra" || "$JOGADA" == "papel" || "$JOGADA" == "tesoura" ]]; then
    echo "Enviando '$JOGADA' para o servidor $SERVER_IP..."
    # Envia a jogada usando netcat
    echo "$JOGADA" | nc -N $SERVER_IP $PORT
    echo "Jogada enviada! Verifique o resultado no terminal do Servidor."
else
    echo "Erro: Jogada inválida."
fi
