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

# Importa a biblioteca nativa 'random', que fornece funções para gerar números aleatórios.
import random

# A função 'random.sample' escolhe uma quantidade específica de números únicos.
# - range(1, 51): Define o intervalo de números possíveis (de 1 até 50).
# - 5: É a quantidade de números que serão sorteados.
# O resultado é guardado na variável 'lista_aleatoria'.
lista_aleatoria = random.sample(range(1, 51), 5)

# Inicia um loop infinito. Isso serve para "prender" o usuário no jogo 
# até que ele digite um número válido.
while True:
    # O bloco 'try' tenta executar o código. Se algo der errado (como tentar 
    # converter uma letra em número), ele pula direto para o bloco 'except'.
    try:
        # Pede o palpite do usuário e converte o texto recebido em um número inteiro (int)
        palpite = int(input("Digite o seu palpite: "))
        
        # O operador 'in' verifica se o palpite do usuário existe DENTRO da lista sorteada
        if palpite in lista_aleatoria:
            print("Parabéns! você acertou!")
        else:
            print("Você errou!")
            # Mostra quais eram os números vencedores caso ele tenha errado
            print(f"Numeros sorteados: {lista_aleatoria}")
            
        # O 'break' encerra o loop 'while'. Note que ele é acionado tanto se o 
        # usuário acertar quanto se ele errar. Ou seja, o jogo só tem 1 rodada válida.
        break
        
    # Se o usuário digitar "dez" ou apenas apertar Enter, a conversão para 'int' falha
    # e gera um 'ValueError'. O except captura isso e impede que o programa quebre.
    except ValueError:
        print("Palpite inválido, tente novamente!")
    

