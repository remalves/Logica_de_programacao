''''Faça um programa que solicite do usuário os elementos de uma matriz 3
x 2 (matriz A). Em seguida, o programa deverá criar a matriz transposta
de A (At). Ao final, deve ser mostrada a matriz original e sua respectiva
transposta. Lembre-se que a matriz transposta At será obtida a partir da
matriz A trocando-se ordenadamente as linhas por colunas (ou as
colunas por linhas), como no exemplo a seguir:'''

matrizA=[]

N = 3
M = 2

for i in range(N):
    lista = []
    for j in range(M):
        num=int(input('Digite um valor: '))
        lista.append(num)
    matrizA.append(lista)

matrizT=[]
for j in range(M):
    lista2=[]
    for i in range(N):
        num2 = matrizA[i][j] 
        lista2.append(num2)
    matrizT.append(lista2)

for i in range(len(matrizT)):
    for j in range(len(matrizT[i])):
        print(matrizT[i][j], end=' ')
    print()
