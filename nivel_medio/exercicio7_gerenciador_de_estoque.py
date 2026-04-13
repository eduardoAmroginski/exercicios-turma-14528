# Exercício 7: Gerenciador de Estoque
# Módulos aplicados: Aulas 12, 13 e 14.
# Crie um dicionário para simular um estoque de loja, onde a chave é o nome do produto e o
# valor é a quantidade (ex: {'teclado': 10, 'mouse': 5}).
# 1. Crie um loop que pergunte ao usuário: “Qual produto deseja vender?” e “Quantas unida-
# des?”.
# 2. Verifique se o produto existe no dicionário. Se não existir, exiba “Produto não cadastrado”.
# 3. Se existir, verifique se há quantidade suficiente. Se houver, subtraia o valor do estoque e
# exiba a venda confirmada. Se não houver, exiba “Estoque insuficiente”.
# 4. Digitar ”sair” deve encerrar o programa.
# 5. No final, use um laço for com .items() para imprimir o estoque final atualizado.


import os
import time

# --- 1. VARIÁVEL GLOBAL (O BANCO DE DADOS DA LOJA) ---
estoque = {
    'teclado': 10,
    'mouse': 5,
    'monitor': 3,
    'headset': 8
}

# --- 2. FUNÇÕES DE INTERFACE (EXIBIÇÃO NA TELA) ---
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_cabecalho():
    limpar_tela()
    print("--- SISTEMA DE GERENCIAMENTO DE ESTOQUE ---")
    print(f"Estoque Disponível: {list(estoque.keys())}\n")

def mostrar_relatorio_final():
    limpar_tela()
    print("\n--- RELATÓRIO DO ESTOQUE FINAL ---")
    for item, qtd in estoque.items():
        if qtd == 0:
            print(f"🔴 {item.capitalize()}: {qtd} (ESGOTADO)")
        else:
            print(f"🟢 {item.capitalize()}: {qtd} unidades")

# --- 3. FUNÇÕES DE LÓGICA E PROCESSAMENTO ---
def solicitar_quantidade(produto):
    # Pede a quantidade ao usuário e garante que seja um número válido.
    while True:
        try:
            quantidade = int(input(f"Quantas unidades de '{produto}' deseja vender? "))
            if quantidade <= 0:
                print("⚠️ A quantidade deve ser maior que zero. Tente novamente.")
                continue
            return quantidade
        except ValueError:
            print("⚠️ Erro: Por favor, digite um número inteiro válido.")

def processar_venda(produto, quantidade_solicitada):
    # Verifica se há estoque e, se houver, conclui a venda.
    # Como vamos alterar o estoque (dicionário mutável), modificamos direto na chave
    quantidade_disponivel = estoque[produto]
    
    if quantidade_solicitada > quantidade_disponivel:
        print(f"❌ Estoque insuficiente. Temos apenas {quantidade_disponivel} unidades de '{produto}'.")
    else:
        estoque[produto] -= quantidade_solicitada
        print(f"✅ Venda confirmada! {quantidade_solicitada} unidade(s) de '{produto}' vendida(s).")
    
    # Pausa rápida para o usuário ler a mensagem antes de limpar a tela
    time.sleep(2)

# --- 4. FUNÇÃO PRINCIPAL (CONTROLADOR DO FLUXO) ---
def menu_vendas():
    while True:
        mostrar_cabecalho()
        
        produto = input("Qual produto deseja vender? (ou 'sair' para encerrar): ").lower()
        
        # Condição de saída
        if produto == 'sair':
            break

        # Verifica existência do produto
        if produto not in estoque:
            print("❌ Produto não cadastrado.")
            time.sleep(2)
            continue
        
        # Se chegou aqui, o produto existe. Chama as funções auxiliares:
        quantidade = solicitar_quantidade(produto)
        processar_venda(produto, quantidade)
        
    # Quando o loop while for quebrado, encerra mostrando o relatório
    mostrar_relatorio_final()

# --- 5. EXECUÇÃO ---
menu_vendas()