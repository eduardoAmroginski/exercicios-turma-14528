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

def cadastrar_usuario():
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            
            if idade < 0 or idade > 120:
                print("Idade inválida, a idade deve ser entre 0 e 120")
                continue
            
            break
            
        except:
            print("Idade invalida! Digite apenas numeros inteiros positivos!")
    
    nome_usuario = input("Digite o nome do usuário: ")
    
    return {nome_usuario : idade}


print(cadastrar_usuario())