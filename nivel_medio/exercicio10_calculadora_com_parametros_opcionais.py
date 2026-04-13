# Exercício 10: Calculadora com Parâmetros Opcionais
# Módulos aplicados: Aulas 15 e 16.
# Crie uma função chamada calcular_salario que receba três parâmetros:
# - valor_base (obrigatório, float).
# - horas_extras (opcional, int, valor padrão = 0).
# - bonificacao (opcional, bool, valor padrão = False).
# A lógica da função deve ser:
# 1. O salário começa com o valor_base.
# 2. Cada hora extra vale R$ 50.00. Some as horas extras multiplicadas por 50 ao salário.
# 3. Se bonificacao for True, adicione 15% ao valor total acumulado até o momento.
# 4. Retorne o salário final formatado.
# Chame a função de 3 formas diferentes no seu script para testar: passando apenas o valor base,
# passando valor base e horas extras, e passando todos os parâmetros.


def calcular_salario(valor_base, horas_extras=0, bonificacao=False):
    # 1. O salário começa com o valor base
    salario = valor_base
    
    # 2. Calcula as horas extras (se horas_extras for 0, soma 0)
    valor_das_horas = horas_extras * 50.00
    salario += valor_das_horas
    
    # 3. Aplica a bonificação se for True (15% sobre o valor acumulado)
    if bonificacao:
        salario += salario * 0.15
        
    # 4. Retorna o salário formatado
    return f"R$ {salario:.2f}"

# --- TESTANDO A FUNÇÃO EM 3 CENÁRIOS DIFERENTES ---

print("--- CALCULADORA DE SALÁRIO ---")

# Cenário 1: Passando APENAS o valor base (os outros assumem o valor padrão)
# Esperado: 3000.00
salario_1 = calcular_salario(3000.00)
print(f"Cenário 1 (Apenas Base): {salario_1}")

# Cenário 2: Passando valor base e horas extras (bonificação assume False)
# Esperado: 3000.00 + (10 * 50) = 3500.00
salario_2 = calcular_salario(3000.00, 10)
print(f"Cenário 2 (Base + 10h Extras): {salario_2}")

# Cenário 3: Passando todos os parâmetros
# Esperado: 3500.00 + 15% = 4025.00
salario_3 = calcular_salario(3000.00, 10, True)
print(f"Cenário 3 (Base + 10h Extras + Bonificação): {salario_3}")

# --- BÔNUS: Cenário 4 (Nomeando parâmetros/Keyword arguments) ---
# Se você quiser passar a bonificação mas NENHUMA hora extra, 
# você pode chamar o parâmetro pelo nome:
# Esperado: 3000.00 + 15% = 3450.00
salario_4 = calcular_salario(3000.00, bonificacao=True)
print(f"Cenário Bônus (Base + Bonificação direto): {salario_4}")