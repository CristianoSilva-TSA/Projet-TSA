import random
import time

def mostrar_opcoes():
    """Imprime as regras do jogo."""
    print("\n-------------------------------------------")
    print("      (Pedra, Papel, Tesoura)")
    print("-------------------------------------------")
    print("Regras:")
    print("  - Pedra vence Tesoura")
    print("  - Papel vence Pedra")
    print("  - Tesoura vence Papel")
    print("Digite 'sair' a qualquer momento para terminar.")
    print("-------------------------------------------\n")

def jogar_ppt():
    """Função principal que executa o jogo."""
    
    opcoes_validas = ["pedra", "papel", "tesoura"]
    pontuacao_jogador = 0
    pontuacao_computador = 0

    mostrar_opcoes()
    
    while True: # Loop principal do jogo

        # 1. Escolha do Jogador
        escolha_jogador = input("Escolha (Pedra, Papel ou Tesoura): ").lower().strip()
        
        # Opção para sair do jogo
        if escolha_jogador == 'sair':
            print("\n-------------------------------------------")
            print(f"👋 Jogo terminado. Resultado final: Jogador {pontuacao_jogador} x {pontuacao_computador} Computador.")
            print("-------------------------------------------")
            break

        # Validação da escolha
        if escolha_jogador not in opcoes_validas:
            print("🚫 Opção inválida. Por favor, escolha 'Pedra', 'Papel' ou 'Tesoura'.")
            continue

        # 2. Escolha do Computador
        escolha_computador = random.choice(opcoes_validas)
        
        print("\n...")
        time.sleep(0.5) # Pausa para dar um efeito de suspense
        print(f"O computador escolheu: {escolha_computador.capitalize()}!")

        # 3. Lógica do Jogo
        if escolha_jogador == escolha_computador:
            resultado = "🤝 Empate!"
        elif (
            (escolha_jogador == "pedra" and escolha_computador == "tesoura") or
            (escolha_jogador == "papel" and escolha_computador == "pedra") or
            (escolha_jogador == "tesoura" and escolha_computador == "papel")
        ):
            resultado = "🎉 Você Ganhou!"
            pontuacao_jogador += 1
        else:
            resultado = "🤖 O Computador Ganhou!"
            pontuacao_computador += 1

        # 4. Mostrar Resultados e Pontuação
        print(resultado)
        print(f"📊 Pontuação atual: Jogador {pontuacao_jogador} x {pontuacao_computador} Computador\n")


# Iniciar o jogo
if __name__ == "__main__":
    jogar_ppt()
