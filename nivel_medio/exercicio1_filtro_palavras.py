# Exercício 1: O Filtro de Palavras
# Módulos aplicados: Aulas 02, 04, 07, 10 e 11.
# Crie um script que peça ao usuário para digitar uma frase longa. Seu programa deve:
# 1. Remover os espaços em branco extras no início e no fim da frase.
# 2. Converter toda a frase para letras minúsculas.
# 3. Transformar a frase em uma lista de palavras.
# 4. Usar um laço for para iterar sobre essa lista e construir uma nova lista contendo apenas
# as palavras que:
#   - Tenham mais de 4 letras.
#   - Não comecem com a letra ‘a’.
# 5. Ao final, imprima a lista filtrada e a quantidade de palavras que passaram no filtro.


# Solicita uma frase ao usuário, remove espaços extras no início e no fim (.strip()),
# converte todas as letras para minúsculas (.lower()) e 
# divide a frase em uma lista de palavras separadas por espaço (.split(" "))
frase = input("Digite uma frase longa: ").strip().lower().split(" ")

# Define uma função chamada 'filtrar_palavras' que recebe a lista de palavras
def filtrar_palavras(frase):
    # Cria uma lista vazia para armazenar as palavras que passarem pelo filtro
    palavras_filtrada = []
    
    # Inicia um laço de repetição que vai percorrer cada palavra dentro da lista
    for palavra in frase:
        # Verifica duas condições ao mesmo tempo:
        # 1. Se a palavra tem mais de 4 letras: len(palavra) > 4
        # 2. Se a primeira letra da palavra [0] NÃO é 'a': not(palavra[0] == 'a')
        if (len(palavra) > 4) and not(palavra[0] == 'a'):
            # Se a palavra cumprir as duas regras, ela é adicionada à lista de filtradas
            palavras_filtrada.append(palavra)
    
    # Após verificar todas as palavras, a função retorna a nova lista filtrada
    return palavras_filtrada

# Chama a função passando a lista criada na primeira linha e 
# guarda o resultado retornado dentro da variável 'filtrado'
filtrado = filtrar_palavras(frase)

# Imprime na tela a quantidade de itens presentes na lista filtrada usando len()
print(f"Quantidade de palavras filtradas: {len(filtrado)}")

# Imprime a lista final contendo apenas as palavras que passaram no filtro
print(filtrado)