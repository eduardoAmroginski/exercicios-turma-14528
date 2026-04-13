# Exercício 6: O Jogo da Forca Simplificado
# Módulos aplicados: Aulas 06, 07, 10 e 19.
# Crie uma versão simplificada do jogo da forca.
# 1. Defina uma variável com a palavra secreta (ex: palavra = "python").
# 2. Crie uma lista vazia chamada letras_descobertas.
# 3. Dê ao usuário 5 tentativas. Use um while para controlar o jogo.
# 4. A cada rodada, exiba a palavra ocultando as letras não descobertas com ” _ ” (use um for
# na palavra secreta junto com o operador in na lista de letras descobertas).
# 5. Peça uma letra. Se a letra estiver na palavra secreta, adicione-a à lista letras_descobertas.
# Se não estiver, diminua 1 tentativa.
# 6. O jogo acaba se ele descobrir todas as letras (vitória) ou as tentativas chegarem a zero
# (derrota).

import os


def jogar_forca():
    print("--- BEM-VINDO AO JOGO DA FORCA SIMPLIFICADO ---")
    
    # 1. Defina uma variável com a palavra secreta
    palavra = "python"
    
    # 2. Crie uma lista vazia chamada letras_descobertas
    letras_descobertas = []
    
    # 3. Dê ao usuário 5 tentativas e use um while
    tentativas = 5
    
    while tentativas > 0:
        # 4. Exiba a palavra ocultando as letras não descobertas com " _ "
        palavra_exibida = ""
        for letra in palavra:
            if letra in letras_descobertas:
                palavra_exibida += letra + " "
            else:
                palavra_exibida += "_ "
                
        print(f"\nPalavra: {palavra_exibida}")
        print(f"Tentativas restantes: {tentativas}")
        
        # 6. O jogo acaba se ele descobrir todas as letras (vitória)
        # Se não tem mais underline na palavra que estamos exibindo, ele acertou tudo
        if "_" not in palavra_exibida:
            print("\n🎉 Parabéns! Você descobriu a palavra e VENCEU o jogo!")
            break
            
        # 5. Peça uma letra
        chute = input("Digite uma letra: ").lower()
        
        # Pequena validação para evitar erros do usuário
        if len(chute) != 1 or not chute.isalpha():
            print("⚠️ Por favor, digite apenas uma letra válida.")
            continue
            
        if chute in letras_descobertas:
            print("⚠️ Você já tentou essa letra. Tente outra!")
            continue

        # 5. Se a letra estiver na palavra secreta, adicione-a à lista
        if chute in palavra:
            print("✅ Acertou! Essa letra faz parte da palavra.")
            letras_descobertas.append(chute)
        # 5. Se não estiver, diminua 1 tentativa
        else:
            print("❌ Errou! Essa letra não existe na palavra.")
            tentativas -= 1

    # 6. O jogo acaba se as tentativas chegarem a zero (derrota)
    if tentativas == 0:
        print("\n💀 Fim de jogo! Você foi enforcado.")
        print(f"A palavra secreta era: {palavra.upper()}")

# Executa o jogo
jogar_forca()