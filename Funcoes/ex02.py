#Exemplo: Função para somar dois números

#função
def soma(a,b):
    r = a+b 
    print(r)

#main = programa principal
print("Bem-vindo ao programa")
soma(2,3)


#ou

def soma(a,b):
    r = a+b
    return r

resultado = soma(2,3)
print('resultado da soma: ', resultado)