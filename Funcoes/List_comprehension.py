def par(num):
    if num % 2 == 0:
        return True
    else:
        return False
    

def pares_ate(n):
    lista_pares = [num for num in range(2, n) if par(num)]
    return lista_pares

meus_pares = pares_ate(20) 
print('Meus pares = ', meus_pares)