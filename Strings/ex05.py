''' É possível descobrir o chamado valor ordinal de um caractere
utilizando a função ord:'''

print(ord("A"))
print(ord("B"))
print(ord("5"))
print(ord("a"))
print("apple" > "Apple")

'''O laço while também pode ser usado para percorrer uma string'''
fruta = "apple"
i = 0
while i < len(fruta):
    print(fruta[i])
    i += 1
'''
Varredura com for
O laço for pode ser usado para iterar sobre os caracteres de uma string (cada posição dentro da string)
Exemplo:'''
fruta = "apple"
for i in range(len(fruta)):
 atual = fruta[i]
 print(atual)
