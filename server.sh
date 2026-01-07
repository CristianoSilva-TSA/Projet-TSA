#!/bin/bash

PORT=5000

echo "-------------------------------------------"
echo "  RPS SERVER - Árbitro Online Iniciado"
echo "  A aguardar jogadores na porta $PORT..."
echo "-------------------------------------------"

# Criar pipes para gerir os dados
mkfifo pipe1 pipe2 2>/dev/null

while true; do
    echo "Aguardando Jogador 1..."
    # Recebe a jogada do Jogador 1
    J1_DATA=$(nc -l -p $PORT)
    echo "Jogador 1 enviou a jogada."

    echo "Aguardando Jogador 2..."
    # Recebe a jogada do Jogador 2
    J2_DATA=$(nc -l -p $PORT)
    echo "Jogador 2 enviou a jogada."

    echo "Calculando resultado: J1:$J1_DATA vs J2:$J2_DATA"

    if [ "$J1_DATA" == "$J2_DATA" ]; then
        RESULTADO="Empate!"
    elif [[ ("$J1_DATA" == "pedra" && "$J2_DATA" == "tesoura") || 
            ("$J1_DATA" == "papel" && "$J2_DATA" == "pedra") || 
            ("$J1_DATA" == "tesoura" && "$J2_DATA" == "papel") ]]; then
        RESULTADO="Jogador 1 venceu!"
    else
        RESULTADO="Jogador 2 venceu!"
    fi

    echo "--- Fim da Rodada: $RESULTADO ---"
    echo "Pronto para nova partida..."
done
