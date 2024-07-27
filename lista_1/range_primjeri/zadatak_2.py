lista_imena = ["Hana", "Martina", "Andrija", "Luka", "Zvonimir", "Lucija"]
#               1        2          3         1        2           3
#               0        1          2         3         4          5


broj_timova = 3
redni_broj_tima_1 = 0
redni_broj_tima_2 = 1
redni_broj_tima_3 = 2


print("Tim 1:")
for indeks in range(redni_broj_tima_1, len(lista_imena), broj_timova):
    print(f"\t{lista_imena[indeks]}")

print("\n\n")
print("Tim 2:")
for indeks in range(redni_broj_tima_2, len(lista_imena), broj_timova):
    print(f"\t{lista_imena[indeks]}")

print("\n\n")
print("Tim 3:")
for indeks in range(redni_broj_tima_3, len(lista_imena), broj_timova):
    print(f"\t{lista_imena[indeks]}")
