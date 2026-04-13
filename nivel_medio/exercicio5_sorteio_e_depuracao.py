# Exercício 5: Sorteio e Depuração
# Módulos aplicados: Aulas 18 e 19.
# Neste exercício, o foco é escrever um código limpo (seguindo a PEP 8) e usar ferramentas nati-
# vas.
# 1. Importe a biblioteca random.
# 2. Gere uma lista com 5 números inteiros aleatórios entre 1 e 50.
# 3. Peça para o usuário tentar adivinhar um número (use try/except para o input).
# 4. Use o operador in para verificar se o palpite do usuário está dentro da lista sorteada.
# 5. Se acertar, dê os parabéns. Se errar, mostre a lista com os números que haviam sido sor-
# teados.

import random

lista_aleatoria = random.sample(range(1, 51), 5)

while True:
    try:
        palpite = int(input("Digite o seu palpite: "))
        
        if palpite in lista_aleatoria:
            print("Parabéns! você acertou!")
        else:
            print("Você errou!")
            print(f"Numeros sorteados: {lista_aleatoria}")
        break
    except ValueError:
        print("Palpite inválido, tente novamente!")
    
    

