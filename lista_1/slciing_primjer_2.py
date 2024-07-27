lista_imena = ["Marko", "Hana", "Ivana", "Mario", "Nikola", "Andro", "Karla"]
#                0        1        2        3        4        5         6
#               -7      -6        -5        -4        -3        -2         -1

# print(lista_imena[-3])
# print(lista_imena[-7])

# print(lista_imena[-3:])

# print(lista_imena[-1:2:-2])

# antipattern kada mjesmao pozitive i negative indekse
# print(lista_imena[-4:1:-3])

korak_1 = lista_imena[-4:]
korak_2 = korak_1[::-1]

ekvivalento = korak_1[3::-1]

print(korak_2)
print(ekvivalento)

plitka_kopija = lista_imena[::]

plitka_kopija[3] = "Havana"

print(lista_imena)
print(plitka_kopija)
