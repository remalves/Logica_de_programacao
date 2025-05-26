#Funções que produzem listas
#Função: entrada=n e saída=lista_pares

def pares_ate(n):
    print('Lista Pares: ')
    lista_pares=[]
    for i in range(2,n):
        if i%2 ==0:
            lista_pares.append(i)
    return lista_pares


meus_pares = pares_ate(50)
print(meus_pares)