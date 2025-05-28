''''Escreva um programa que leia inteiros positivos m e n e os elementos
de uma matriz A de números inteiros de dimensão m x n e ao final
mostra a quantidade de linhas e colunas que tem apenas zeros (linhas
nulas e colunas nulas).'''

m = int(input('qtd de linhas: '))
n = int(input('qtd de colunas: '))

mA=[]
for i in range(m):
    lista=[]
    for j in range(n):
        num = int(input('valor: '))
        lista.append(num)
    mA.append(lista)

linhas_nulas = 0
for i in range(len(mA)): 
    eh_nula = True
    for j in range(len(mA[i])):
        if mA[i][j] != 0:
            eh_nula = False
    if eh_nula:
            linhas_nulas+=1

col_nulas = 0
for i in range(len(mA[i])): #percorre colunas 
    eh_nula = True
    for j in range(len(mA)): #percorre linhas
        if mA[j][i] != 0:
            eh_nula = False
    if eh_nula:
            col_nulas+=1

print(f'linhas nulas: {linhas_nulas} e colunas nulas: {col_nulas}')


            

            






