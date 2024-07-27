lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]

# [4, 5, 6] uhu ljepilo [1, 2, 3]
lista_3 = lista_2 + lista_1
# ekvivalentno
# print(lista_1.__add__(lista_2))
print(lista_3)

lista_a = [1, 2, 3]
lista_a = lista_a * 3
print(lista_a)

voce = ["jabuka", "kruska", "sljiva"]
print("jabuka" in voce)
print("lubenica" not in voce)

print("\n\n\n")
druga_lista = [1, 2, 3]
print(lista_1 == druga_lista)
print(id(lista_1))
print(id(druga_lista))

moj_string = "banana"
moj_string_list = list(moj_string)
print(moj_string_list)
