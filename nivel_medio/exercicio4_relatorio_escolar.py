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

# Lista de dicionários simulando um pequeno banco de dados.
# Cada dicionário representa um aluno com sua respectiva chave "nome" (string) e "notas" (lista de floats).
lista = [
    {"nome": "Kleber Silva", "notas": [7.5, 9.8, 3.4]},
    {"nome": "Maria Joaquina", "notas": [9.5, 9.8, 8.4]},
    {"nome": "Frederico Gutierres", "notas": [5.5, 4.3, 9.4]}
]

# Função principal de processamento de dados.
# Recebe a lista completa de alunos e categoriza quem passou e quem reprovou.
def analisar_turma(lista_alunos):
    # Cria duas listas vazias que armazenarão apenas os nomes dos alunos.
    alunos_aprovados = []
    alunos_reprovados = []
    
    # Percorre a lista de dicionários, processando um aluno por vez.
    for aluno in lista_alunos:
        # Pega a lista de notas do aluno atual e envia para a função auxiliar de cálculo.
        media = calcular_media(aluno["notas"])
        
        # Aplica a regra de negócio: média maior ou igual a 7.0 aprova.
        if media >= 7.0:
            alunos_aprovados.append(aluno["nome"])
        else:
            alunos_reprovados.append(aluno["nome"])
    
    # Retorna as duas listas de uma vez. 
    # O Python junta isso automaticamente em uma estrutura chamada "Tupla" para enviar de volta.
    return alunos_aprovados, alunos_reprovados

# Função auxiliar matemática: responsabilidade estrita de calcular a média.
def calcular_media(notas): 
    # O sum(notas) faz o for e a soma internamente em C, sendo muito mais rápido!
    return sum(notas) / len(notas)

# Função de interface (Visual): recebe uma lista e um título e imprime na tela.
def mostrar_lista(lista, tipo):
    print(f"---- Lista {tipo} -----")
    for aluno in lista:
        print(f" - {aluno}")


# --- EXECUÇÃO DO PROGRAMA ---

# Aqui acontece o "Unpacking" (Desempacotamento). 
# A função 'analisar_turma' retorna uma Tupla com duas listas. 
# O Python automaticamente joga a primeira lista na variável 'lista_aprovados' e a segunda na 'lista_reprovados'.
lista_aprovados, lista_reprovados = analisar_turma(lista)

# Passa as listas já separadas para a função responsável por desenhar isso no terminal.
mostrar_lista(lista_aprovados, "APROVADOS")
mostrar_lista(lista_reprovados, "REPROVADOS")
