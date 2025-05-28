'''texto = "Essa é uma 'string'"
print(texto)
texto[2] = 'S'
print(texto)


Como strings são IMUTÁVEIS, caso você precise de uma string
diferente, é necessário criar uma nova utilizando, caso desejar,
fatias (partes) de outras strings
'''

texto = "Essa é uma 'string'"
print(texto)
novo_texto = 'Mais' + texto[6:] #fatiamento e concatenação
print(novo_texto)
