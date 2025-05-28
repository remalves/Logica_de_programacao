'''Escreva um programa que remove a primeira ocorrência de uma letra de
uma string. A string e a letra devem ser fornecidas pelo usuário.
'''

texto = input("Escreva uma palavra: ")
letra = input("Escreva uma letra: ")


while letra not in texto: 
    print('A letra nao esta na palavra digitada')
    letra = input("Escreva uma letra: ")


novo_texto = texto.replace(letra,'',1)
print('Resultado: ', novo_texto)
