# Exercício 8: Frequência de Caracteres
# Módulos aplicados: Aulas 07 e 12.
# Crie um programa que conte quantas vezes cada letra aparece em uma string.
# 1. Peça ao usuário para digitar uma palavra ou frase.
# 2. Crie um dicionário vazio chamado contagem.
# 3. Use um laço for para passar por cada caractere da string.
# 4. Se o caractere já for uma chave no dicionário, some 1 ao seu valor. Se não for, crie a chave
# no dicionário com o valor 1.
# 5. Ignore os espaços em branco (não os adicione ao dicionário).
# 6. Imprima o dicionário final para mostrar a frequência de cada letra.


def contar_caracteres():
    print("--- CONTADOR DE FREQUÊNCIA DE LETRAS ---")
    
    # 1. Peça ao usuário para digitar uma palavra ou frase
    # Usamos .lower() como uma boa prática para que 'A' e 'a' não sejam contadas como letras diferentes
    frase = input("Digite uma palavra ou frase: ").lower()
    
    # 2. Crie um dicionário vazio chamado contagem
    contagem = {}
    
    # 3. Use um laço for para passar por cada caractere da string
    for caractere in frase:
        # 5. Ignore os espaços em branco
        if caractere == ' ':
            continue # O continue pula para o próximo caractere sem executar o código abaixo
            
        # 4. Lógica de contagem
        if caractere in contagem:
            # Se a chave já existe, apenas somamos +1 ao valor atual
            contagem[caractere] += 1
        else:
            # Se a chave não existe, criamos ela agora e dizemos que apareceu 1 vez
            contagem[caractere] = 1
            
    # 6. Imprima o dicionário final para mostrar a frequência
    print("\n--- RESULTADO ---")
    
    # Formatando a saída para ficar mais bonita e fácil de ler
    for letra, frequencia in contagem.items():
        print(f"A letra '{letra}' apareceu {frequencia} vez(es).")

# Executa o programa
contar_caracteres()