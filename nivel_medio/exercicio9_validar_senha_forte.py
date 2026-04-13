# Exercício 9: Validador de Senha Forte
# Módulos aplicados: Aulas 04, 15 e 18.
# Crie uma função chamada validar_senha(senha) que recebe uma string e retorna um valor bo-
# oleano (True ou False). A senha só será considerada forte (True) se cumprir todos os requisitos
# abaixo:
# 1. Ter pelo menos 8 caracteres de comprimento.
# 2. Conter pelo menos um número (Dica: você pode percorrer a string e usar o método
# .isdigit()).
# 3. Conter pelo menos uma letra maiúscula (.isupper()).
# 4. Conter pelo menos uma letra minúscula (.islower()).
# Escreva o código de forma limpa (Clean Code), evitando blocos de if/else desnecessariamente
# aninhados (Dica: use a técnica de retorno antecipado/Early Return). Peça uma senha ao usuário
# e teste sua função.


def validar_senha(senha):
    # 1ª Barreira: Comprimento mínimo
    # (Retorno antecipado: se for menor que 8, já reprova na hora)
    if len(senha) < 8:
        return False
        
    # Inicializando as "bandeiras" para as outras verificações
    tem_numero = False
    tem_maiuscula = False
    tem_minuscula = False
    
    # Percorrendo a string caractere por caractere
    for char in senha:
        if char.isdigit():
            tem_numero = True
        elif char.isupper():
            tem_maiuscula = True
        elif char.islower():
            tem_minuscula = True
            
    # 2ª, 3ª e 4ª Barreiras: Verificando as bandeiras
    # (Mais retornos antecipados para manter o código plano, sem else)
    if not tem_numero:
        return False
        
    if not tem_maiuscula:
        return False
        
    if not tem_minuscula:
        return False
        
    # Se passou por todas as barreiras acima, a senha é impecável!
    return True

# SIMPLIFICANDO AINDA MAIS, utilizando o ANY()
# def validar_senha_pro(senha):
#     if len(senha) < 8:
#         return False
        
#     # Verifica se NÃO tem (not any) NENHUM número na senha
#     if not any(char.isdigit() for char in senha):
#         return False
        
#     if not any(char.isupper() for char in senha):
#         return False
        
#     if not any(char.islower() for char in senha):
#         return False
        
#     return True


# --- TESTANDO A FUNÇÃO ---
print("--- VALIDADOR DE SENHA FORTE ---")
print("Regras: Mínimo de 8 caracteres, 1 número, 1 maiúscula e 1 minúscula.")

senha_usuario = input("Digite uma senha para testar: ")

if validar_senha(senha_usuario):
    print("✅ Senha FORTE! Aprovada.")
else:
    print("❌ Senha FRACA! Ela não atende a todos os requisitos.")