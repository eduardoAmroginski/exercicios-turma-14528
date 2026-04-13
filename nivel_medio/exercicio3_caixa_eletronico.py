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

import os
import time

TEMPO = 3
TEMPO_VER_SALDO = 5

def mostrar_opcoes():
    print("1- Sacar")
    print("2- Depositar")
    print("3- Ver Saldo")
    print("4- Sair")


def sacar(saldo, extrato):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("----- SAQUE -----")
        try:
            valor_saque = float(input("Digite o valor que quer sacar: "))
            
            if valor_saque <= 0:
                print("ERRO: O valor não pode ser menor ou igual a zero, tente novamente.")
                time.sleep(TEMPO)
                break
            elif valor_saque > saldo:
                print("Saldo insuficiente")
                time.sleep(TEMPO)
                break
            else:
                saldo = saldo - valor_saque
                extrato.append(("Saque", valor_saque))
                print("Saque realizado com sucesso!")
                time.sleep(TEMPO)
                break
        except ValueError:
            print("Valor inválido, tente novamente.")  
    return saldo


def depositar(saldo, extrato):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("----- DEPOSITO -----")
        try:
            valor_deposito = float(input("Digite o valor que quer depositar: "))
            if valor_deposito <= 0:
                print("ERRO: O valor não pode ser menor ou igual a zero, tente novamente.")
                time.sleep(TEMPO)
                break
            else:
                saldo = saldo + valor_deposito
                extrato.append(("Deposito", valor_deposito))
                print("Deposito realizado com sucesso!")
                time.sleep(TEMPO)
                break
            
        except:
            print("Valor inválido, tente novamente.")
    return saldo


def ver_saldo(saldo):
    print("----- SALDO -----")
    print(f"Valor na conta: R${saldo:.2f}")
    time.sleep(TEMPO_VER_SALDO)


def ver_extrato(extrato):
    print("----- EXTRATO -----")
    for transacao in extrato:
        print(f"{transacao[0]}: R$ {transacao[1]:.2f}")


def menu():
    
    extrato = []
    saldo = 1000.00
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        mostrar_opcoes()
        opcao = input("Escolha uma opção: ")
        
        match opcao:
            case "1":
                saldo = sacar(saldo, extrato)
            case "2":
                saldo = depositar(saldo, extrato)
            case "3":
                ver_saldo(saldo)
            case "4":
                ver_extrato(extrato)
                print("Finalizando aplicação...")
                break
            

menu()