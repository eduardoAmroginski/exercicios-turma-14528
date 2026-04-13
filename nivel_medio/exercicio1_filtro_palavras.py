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



frase = input("Digite uma frase longa: ").strip().lower().split(" ")

def filtrar_palavras(frase):
    palavras_filtrada = []
    
    for palavra in frase:
        if (len(palavra) > 4) and not(palavra[0] == 'a'):
            palavras_filtrada.append(palavra)
    
    return palavras_filtrada


filtrado = filtrar_palavras(frase)

print(f"Quantidade de palavras filtradas: {len(filtrado)}")
print(filtrado)
