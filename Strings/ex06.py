print('a' in 'a')
print('apple' in 'apple')
print('' in 'a')
print('' in 'apple')

'''Outro exemplo: dada uma palavra, retirar suas vogais e mostra a
nova string'''

palavra=input("Digite uma palavra: ")
vogais = "aeiouAEIOU"
str_sem_vogais = ""
for cada_letra in palavra:
    if cada_letra not in vogais:
        str_sem_vogais = str_sem_vogais + cada_letra

print(str_sem_vogais)


