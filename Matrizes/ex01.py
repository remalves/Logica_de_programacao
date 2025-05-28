'''Crie um programa que solicita do usuário um valor N representando a
quantidade linhas e um valor M representando a quantidade de colunas
de uma matriz. Depois, o programa deverá solicitar do usuário N x M
elementos para serem incluídos na matriz. Por fim, o programa deverá
percorrer a matriz para encontrar e imprimir o seu maior elemento e o
seu menor elemento.'''

N = int(input('Qtd de linhas: '))
M = int(input('Qtd de colunas: '))
matriz=[]
for i in range(N):
    lista=[]
    for j in range(M):
        num = int(input(f'Digite um valor para a linha {i} na coluna {j}: '))
        lista.append(num)
    matriz.append(lista)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=' ')
    print()

maior = matriz[i][j]
menor = matriz[i][j]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] <= menor: 
            menor = matriz[i][j]
        elif matriz[i][j] >= maior:
            maior = matriz[i][j]

print(f'Maior numero: {maior} e menor numero: {menor}')
            

 