'''Faça um programa que solicite do usuário um valor N, representando
a dimensão de uma matriz quadrada (matriz A). Em seguida, o
programa deverá solicitar do usuário os elementos da matriz A e,
posteriormente, deverá verificar se A é simétrica. Obs: Matriz
simétrica: matriz quadrada de ordem n tal que A = A
t'''

N = int(input('Digite um valor para a matriz: '))
matA=[]
for i in range(N):
    listA=[]
    for j in range(N):
        numA=int(input('Digite um valor: '))
        listA.append(numA)
    matA.append(listA)

eh_simetrica = False
for i in range(len(matA)):
    for j in range(len(matA[i])):
        if matA[i][j] == matA[j][i]:
            eh_simetrica = True

if eh_simetrica:
    print("A matriz é simetrica")
else:
    print("A matriz nao eh simetrica")
