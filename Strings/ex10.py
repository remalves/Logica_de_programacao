'''Outro exemplo:'''
food = "banana bread"
print(food.capitalize())
print("*"+food.center(25)+"*")
print("*"+food.ljust(25)+"*")
print("*" +food.rjust(25)+"*")
print(food.find("e"))
print(food.find("na"))
print(food.find("b"))
print(food.rfind("e"))
print(food.rfind("na"))
print(food.rfind("b"))
print(food.index("e"))


'''▪ Teste com os valores Araraquara e depois 1234:'''
teste_str=input("Digite um valor: ")
print(teste_str, " capitalize",teste_str.capitalize())
print(teste_str," center",teste_str.center(20))
print(teste_str," count",teste_str.count("a"))
print(teste_str," find",teste_str.find("ara"))
print(teste_str," isalnum",teste_str.isalnum())
print(teste_str," isalpha",teste_str.isalpha())
print(teste_str," isdigit",teste_str.isdigit())
print(teste_str," replace",teste_str.replace("a","o"))
