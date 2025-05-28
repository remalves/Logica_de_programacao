frase = "Eu posso ajudar respondendo perguntas no fórum!"
sorteio = [5, -4, 3, -8, 11]

acertos = 0
for i in sorteio:
    resposta = input(f"Qual o caractere de índice {i} ")
    if frase[i] == resposta:
        print("Parabéns, você acertou!")
        acertos+=1
    else:
        print(f"Você errou. O caractere de índice {i} é:{frase[i]}")

print(f"Você acertou {acertos} de {len(sorteio)} perguntas.")