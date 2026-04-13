# Exercício 4: Relatório Escolar
# Módulos aplicados: Aulas 13 e 16.
# Crie uma lista contendo pelo menos 3 dicionários. Cada dicionário representa um aluno e deve
# ter duas chaves: 'nome' (uma string) e 'notas' (uma lista com 3 notas do tipo float).
# 1. Crie uma função chamada analisar_turma(lista_alunos).
# 2. A função deve percorrer a lista de dicionários. Para cada aluno, calcule a média das 3
# notas.
# 3. A função deve ter retornos múltiplos: retorne uma lista com o nome dos alunos aprova-
# dos (média ≥ 7.0) e uma segunda lista com o nome dos alunos reprovados.
# 4. Fora da função, chame-a passando sua lista de alunos e desempacote o retorno em duas
# variáveis (aprovados e reprovados). Imprima os resultados de forma amigável.

lista = [
    {"nome": "Kleber Silva", "notas": [7.5, 9.8, 3.4]},
    {"nome": "Maria Joaquina", "notas": [9.5, 9.8, 8.4]},
    {"nome": "Frederico Gutierres", "notas": [5.5, 4.3, 9.4]}
]

def analisar_turma(lista_alunos):
    alunos_aprovados = []
    alunos_reprovados = []
    
    for aluno in lista_alunos:
        media = calcular_media(aluno["notas"])
        
        if media >= 7.0:
            alunos_aprovados.append(aluno["nome"])
        else:
            alunos_reprovados.append(aluno["nome"])
    
    return alunos_aprovados, alunos_reprovados


def calcular_media(notas):
    soma = 0
    for nota in notas:
          soma = soma + nota      
          
    return soma / len(notas)


def mostrar_lista(lista, tipo):
    print(f"---- Lista {tipo} -----")
    for aluno in lista:
        print(f" - {aluno}")


lista_aprovados, lista_reprovados = analisar_turma(lista)

mostrar_lista(lista_aprovados, "APROVADOS")
mostrar_lista(lista_reprovados, "REPROVADOS")

