'''Neste exemplo o programa conta o número de vezes que uma
letra em particular aparece em uma string:'''
palavra=input("Digite uma palavra: ")
caractere=input("Digite um caractere a ser contado: ")

contador = 0
for letra in palavra:
    if letra == caractere:
        contador = contador + 1

print(f"A letra {caractere} aparece {contador} vezes na palavra {palavra}")


'''▪Neste exemplo o programa mostra a posição da primeira
ocorrência de uma letra em particular em uma string:'''

palavra=input("Digite uma palavra: ")
caractere=input("Digite um caractere a ser encontrado: ")
indice = 0
existe_letra = False
while indice < len(palavra) and not existe_letra:
    if palavra[indice] == caractere:
        existe_letra = True
    else:
        indice = indice + 1

if existe_letra:
    print(f"A primeira ocorrência do caractere {caractere} na palavra {palavra} está na posição {indice}")
else:
 print(f"Não há ocorrência do caractere {caractere} na palavra {palavra}!")