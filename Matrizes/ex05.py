'''Escreva um programa que leia inicialmente os elementos de 2
matrizes A e B, sendo A de dimensão m x n e B de dimensão p x q. O
programa deverá criar uma matriz C, representando a matriz produto
de A e B. Ao final, o programa deve mostrar as matrizes A, B e a
matriz C.'''

m = int(input('qtd de linhas: '))
n = int(input('qtd de colunas: '))

mA=[]
for i in range(m):
    lista=[]
    for j in range(n):
        num = int(input('valor: '))
        lista.append(num)
    mA.append(lista)

p = int(input('qtd de linhas: '))
q = int(input('qtd de colunas: '))
if n != p:
    print('Erro: número de colunas de A deve ser igual ao número de linhas de B para multiplicação.')
else:
    mB=[]
    for i in range(p):
        lista2=[]
        for j in range(q):
            num2 = int(input('valor: '))
            lista2.append(num2)
        mB.append(lista2)

    mC=[]
    for i in range(m):
        linha = []
        for j in range(q):
            soma = 0
            for k in range(n):
                soma+=mA[i][k] * mB[k][j]
            linha.append(soma)
        mC.append(linha)

def imprimir_matriz(mat,nome):
    print(f'\nMatriz {nome}: ')
    
    for i in range(len(mat)): 
        for j in range(len(mat[i])):
            print(mat[i][j], end=' ')
        print()

imprimir_matriz(mA,'A')
imprimir_matriz(mB,'B')
imprimir_matriz(mC,'C')
