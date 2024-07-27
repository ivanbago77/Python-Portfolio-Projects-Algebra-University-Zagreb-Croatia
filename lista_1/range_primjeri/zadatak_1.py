lista_imena = ["Hana", "Martina", "Andrija", "Luka", "Zvonimir", "Lucija"]
#               1        2          1         2        1           2
#               0        1          2         3         4          5

# tko pripada ekipi 1, a tko pripada ekipi 2
# ispiste koaj imena pripadaju ekipi 1
# ispiste imena za ekipu 2
# for petlji i range

# for ime in lista_imena:
#     print(ime)

# print("\n\n")
# for indeks in range(6):
#     print(lista_imena[indeks])

# print("\n\n")
# for indeks in range(len(lista_imena)):
#     print(lista_imena[indeks])

broj_timova = 2
redni_broj_tima_1 = 0
redni_broj_tima_2 = 1


print("Tim 1:")
for indeks in range(redni_broj_tima_1, len(lista_imena), broj_timova):
    print(f"\t{lista_imena[indeks]}")

print("\n\n")
print("Tim 2:")
for indeks in range(redni_broj_tima_2, len(lista_imena), broj_timova):
    print(f"\t{lista_imena[indeks]}")
