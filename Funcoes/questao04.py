'''Q4: Crie uma função que receba como parâmetro um número 
inteiro. A função deve retornar um número inteiro, conforme 
a seguir:
1. Retornar 1 se o número recebido é positivo
2. Retornar -1 se o número recebido é negativo
3. Retornar 0 se o número recebido é zero'''
def verifica_inteiro(numero):
    if numero == 0:
        return 0
    elif numero > 0: 
        return 1
    else:
        return -1
    
def main():
    num = int(input("Digite um número"))
    result = verifica_inteiro(num)
    if result == 1:
        print("É um inteiro positivo! ")
    elif result == -1:
        print("É um inteiro negativo!")     
    else:
        print("É zero!")           

main()