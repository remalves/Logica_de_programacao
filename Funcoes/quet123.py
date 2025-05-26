'''Q1: a função inteiropositivo(n) verifica se o valor de entrada é um 
número inteiro positivo e retorna Verdadeiro em caso afirmativo e 
Falso caso contrário.'''
def inteiropositivo(numero):
    try:
        numero = int(numero)
        if numero >= 0:
            return True
        else: 
            return False
    except:
        return False
    
'''Q2: a função inteiro(n) verifica se o valor de entrada é um 
número inteiro positivo e retorna Verdadeiro em caso afirmativo e 
Falso caso contrário.'''
def inteiro(numero):
    try:
        numero = int(numero)
        return True
    except:
        return False
    
'''Q3: a função real(n) verifica se o valor de entrada é um 
número real e retorna Verdadeiro em caso afirmativo e 
Falso caso contrário.'''
def real(numero):
    try:
        numero = float(numero)
        return False
    except:
        return False
  
def main():
    num = input("Digite um número")

    if inteiropositivo(num):
        print("É um inteiro positivo! ")

    else:
        print("Não é um inteiro positivo!") 

    if inteiro(num):
        print("É um inteiro! ")

    else:
        print("Não é um inteiro!")    

    if real(num):
        print("É um número real! ")

    else:
        print("Não é um número real!")    

main()

