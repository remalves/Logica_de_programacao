'''Classificação de Caracteres'''

import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)

'''
O código abaixo verifica se o valor digitado é um número inteiro
positivo e ilustra o uso da constante string.digits:'''

nro_ok=False
while not nro_ok:
    nro=input("Digite um número inteiro positivo: ")
    nro_ok=True
    for i in nro:
        if i not in string.digits:
            nro_ok=False
    
    if not nro_ok:
        print("O valor digitado não é um número inteiro positivo!")        
nro=int(nro) #faz a conversão
print("O valor digitado é: ",nro)

'''
O código abaixo verifica se o valor digitado é um número inteiro
positivo utilizando o método isdigit():'''
nro_ok=False
while not nro_ok:
 nro=input("Digite um número inteiro positivo: ")
 nro_ok = nro.isdigit()
 if not nro_ok:
    print("O valor digitado não é um número inteiro positivo!")
nro=int(nro) #faz a conversão
print("O valor digitado é: ",nro)
