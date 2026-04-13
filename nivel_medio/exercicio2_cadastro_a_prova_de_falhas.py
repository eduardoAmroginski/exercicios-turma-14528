# Exercício 2: Cadastro à Prova de Falhas
# Módulos aplicados: Aulas 06, 08, 12, 15 e 17.
# Crie uma função chamada cadastrar_usuario(). Dentro dela, você deve construir um sistema
# de validação robusto usando um loop cego (while True).
# 1. O programa deve pedir a idade do usuário.
# 2. Use try/except para garantir que o usuário digite um número inteiro. Se ele digitar texto
# (ex: “vinte”), o programa não pode quebrar; deve exibir uma mensagem de erro e pedir a
# idade novamente.
# 3. Se a idade digitada for menor que 0 ou maior que 120, exiba “Idade inválida” e use o
# comando continue para voltar ao início do loop.
# 4. Após passar pela validação da idade, o loop deve ser quebrado (break). Em seguida, peça
# o nome do usuário.
# 5. A função deve retornar um dicionário com as chaves 'nome' e 'idade'. Imprima o retorno
# da função no final do script.

# Define a função responsável por cadastrar um novo usuário
def cadastrar_usuario():
    
    # Inicia um loop infinito. O programa vai ficar "preso" aqui pedindo a idade 
    # repetidas vezes até que o usuário digite um valor válido.
    while True:
        try:
            # Solicita a idade ao usuário e tenta converter o texto digitado (string) 
            # para um número inteiro (int).
            idade = int(input("Digite sua idade: "))
            
            # Validação lógica: verifica se a idade está fora de um limite realista
            if idade < 0 or idade > 120:
                print("Idade inválida, a idade deve ser entre 0 e 120")
                # O 'continue' ignora o resto do código abaixo e faz o loop 'while' recomeçar do zero
                continue
            
            # Se o código chegou até aqui, a idade é um número e está dentro do limite.
            # O 'break' quebra o loop infinito, permitindo que o programa avance para a próxima etapa.
            break
            
        # Se o usuário digitar letras (ex: "vinte") ou ficar vazio, o int() vai falhar.
        # Em vez do programa travar e fechar com uma tela vermelha de erro, 
        # o 'except' captura a falha e exibe uma mensagem amigável.
        except ValueError:
            print("Idade invalida! Digite apenas numeros inteiros positivos!")
    
    # Esta linha só será executada após o loop 'while' ser quebrado com sucesso.
    # Solicita o nome do usuário (aqui não há validação, aceita qualquer texto).
    nome_usuario = input("Digite o nome do usuário: ")
    
    # Cria e retorna um dicionário, usando o nome como "chave" e a idade como "valor".
    return {nome_usuario : idade}

# Executa a função e imprime na tela o dicionário que foi retornado por ela.
print(cadastrar_usuario())