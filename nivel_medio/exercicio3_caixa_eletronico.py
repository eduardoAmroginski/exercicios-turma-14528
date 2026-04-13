# Exercício 3: O Caixa Eletrônico
# Módulos aplicados: Aulas 03, 06, 11 e 19.
# Simule o menu de um caixa eletrônico. O usuário tem um saldo inicial de R$ 1000.00 e uma
# lista vazia chamada extrato. Mostre um menu em loop (while) com as opções: 1- Sacar, 2-
# Depositar, 3- Ver Saldo, 4- Sair.
# 1. Use a estrutura match case (ou if/elif se preferir) para tratar a escolha do usuário.
# 2. Sacar: Peça o valor. Se o valor for maior que o saldo, exiba “Saldo insuficiente”. Caso
# contrário, subtraia do saldo e adicione uma tupla à lista extrato, ex: ('Saque', valor).
# 3. Depositar: Peça o valor, some ao saldo e adicione a tupla ('Deposito', valor) ao extrato.
# 4. Ver Saldo: Exiba o saldo formatado com duas casas decimais.
# 5. Sair: Quebre o loop. Antes de encerrar, faça um laço for na lista extrato e imprima o
# histórico de transações.

# Importa bibliotecas nativas do Python:
# 'os' para interagir com o sistema operacional (limpar a tela)
# 'time' para pausar a execução do programa por alguns segundos
import os
import time

# Constantes globais para facilitar a manutenção.
# Se precisarmos alterar o tempo de espera no futuro, mudamos apenas aqui.
TEMPO = 3
TEMPO_VER_SALDO = 5

# Função simples com responsabilidade única: exibir o menu visual.
def mostrar_opcoes():
    print("1- Sacar")
    print("2- Depositar")
    print("3- Ver Saldo")
    print("4- Sair")


# Função que processa o saque. Recebe o estado atual do 'saldo' e a lista 'extrato'.
def sacar(saldo, extrato):
    # Loop infinito para segurar o usuário na tela de saque até que uma ação válida ocorra.
    while True:
        # Limpa o terminal. Funciona tanto no Windows ('nt' -> 'cls') quanto no Linux/Mac ('clear')
        os.system('cls' if os.name == 'nt' else 'clear')
        print("----- SAQUE -----")
        
        # Bloco de tratamento de erros para evitar que letras quebrem o programa.
        try:
            valor_saque = float(input("Digite o valor que quer sacar: "))
            
            # Validação 1: Evitar valores negativos ou zerados
            if valor_saque <= 0:
                print("ERRO: O valor não pode ser menor ou igual a zero, tente novamente.")
                time.sleep(TEMPO)
                break # Quebra o loop do saque e volta pro menu principal
            
            # Validação 2: Evitar que o usuário saque mais do que tem
            elif valor_saque > saldo:
                print("Saldo insuficiente")
                time.sleep(TEMPO)
                break
            
            # Caminho de Sucesso
            else:
                saldo = saldo - valor_saque # Deduz o valor
                extrato.append(("Saque", valor_saque)) # Adiciona uma Tupla na lista de extrato
                print("Saque realizado com sucesso!")
                time.sleep(TEMPO)
                break
                
        # Captura o erro específico de conversão (ex: se o usuário digitar "dez")
        except ValueError:
            print("Valor inválido, tente novamente.")  
            
    # É fundamental retornar o saldo, modificado ou não, para atualizar a variável principal no menu
    return saldo


# Função que processa o depósito. Segue a mesma lógica estrutural do saque.
def depositar(saldo, extrato):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("----- DEPOSITO -----")
        try:
            valor_deposito = float(input("Digite o valor que quer depositar: "))
            
            # Valida se o depósito faz sentido
            if valor_deposito <= 0:
                print("ERRO: O valor não pode ser menor ou igual a zero, tente novamente.")
                time.sleep(TEMPO)
                break
            else:
                saldo = saldo + valor_deposito # Adiciona o valor
                extrato.append(("Deposito", valor_deposito)) # Registra a Tupla
                print("Deposito realizado com sucesso!")
                time.sleep(TEMPO)
                break
            
        # Captura genérica de erros de input
        except:
            print("Valor inválido, tente novamente.")
            
    # Retorna o novo saldo para o menu principal
    return saldo


# Função para exibir o saldo formatado
def ver_saldo(saldo):
    print("----- SALDO -----")
    # O ': .2f' garante que o número terá exatamente 2 casas decimais (ex: 1000.00)
    print(f"Valor na conta: R${saldo:.2f}")
    time.sleep(TEMPO_VER_SALDO)


# Função para iterar sobre a lista de tuplas e exibir o histórico
def ver_extrato(extrato):
    print("----- EXTRATO -----")
    # Para cada tupla dentro da lista, transacao[0] é o Tipo e transacao[1] é o Valor
    for transacao in extrato:
        print(f"{transacao[0]}: R$ {transacao[1]:.2f}")


# Função controladora (Main) que gerencia o estado da aplicação
def menu():
    
    # Inicializa as variáveis de estado da conta
    extrato = []
    saldo = 1000.00
    
    # Loop principal da aplicação (O Caixa Eletrônico em si)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        mostrar_opcoes()
        opcao = input("Escolha uma opção: ")
        
        # Estrutura de decisão moderna do Python 3.10+ (equivalente ao Switch/Case)
        match opcao:
            case "1":
                # A variável 'saldo' é sobrescrita pelo retorno da função sacar()
                saldo = sacar(saldo, extrato)
            case "2":
                # A variável 'saldo' é sobrescrita pelo retorno da função depositar()
                saldo = depositar(saldo, extrato)
            case "3":
                # Apenas passa o saldo por parâmetro para leitura, sem precisar de retorno
                ver_saldo(saldo)
            case "4":
                # Encerra o caixa eletrônico exibindo o extrato final
                ver_extrato(extrato)
                print("Finalizando aplicação...")
                break # Quebra o loop principal e finaliza o script
            
# Chamada que dá o pontapé inicial na execução do programa
menu()