def double_stuff(lista):
    for posicao in range(len(lista)):
        lista[posicao] = 2 * lista[posicao]


things = [2,5,9]
print(things)

double_stuff(things)
print(things)