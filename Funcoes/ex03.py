#Exemplo: Operações com 2 números inteiros

def leitura():
    nro = int(input("Digite um numero inteiro: "))
    return(nro)

def soma(n1,n2):
    return n1+n2

def subtraia(n1,n2):
    return n1-n2

def multiplique(n1,n2):
    return n1*n2

def divida(n1,n2):
    return n1/n2

def main():
    op = input("Escolha uma operacao(+, - , *, / ): ")
    nro1=leitura()
    nro2=leitura()
    if op == '+':
        print('resultado: ' , soma(nro1, nro2))
    elif op == '-':
        print('resultado: ' , subtraia(nro1, nro2))
    elif   op == '*':
        print('resultado: ' , multiplique(nro1, nro2))
    elif op == '/':
        print('resultado: ' , divida(nro1, nro2))
    else:
        print('operacao invalida')

#exemplo de inicio de execução
main()
    