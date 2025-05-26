'''Q5: Faça uma função que receba quatro valores reais 
(faça a consistência), referentes as notas que um aluno 
obteve nos bimestres. A função deve retornar a média final 
desse aluno. Pesquise como arredondar a nota). 
Faça uma função que receba quatro valores, referentes as 
notas que um aluno obteve nos bimestres. A função deve 
retornar Verdadeiro se o aluno foi aprovado e Falso caso 
contrário.'''
def real(numero):
    try:
        numero = float(numero)
        return True
    except:
        return False
    
def calcular_media(lista_notas):
    import math
    soma = 0
    for i in range(len(lista_notas)):
        soma+= lista_notas[i]
    return (soma/len(lista_notas))

def main():
    notas = []
    cont = 0
    while cont < 4:
        num = input("Digite um número")
        if real(num):
            num = float(num)
            cont+=1
            notas.append(num)
    media = calcular_media(notas)
    print(media)
                

main()