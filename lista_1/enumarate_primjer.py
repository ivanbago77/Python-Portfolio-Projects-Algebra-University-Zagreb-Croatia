lista_imena = ["Hana", "Vana", "Mario", "Ivana"]

for indeks in range(len(lista_imena)):
    print(f"{indeks + 1}. {lista_imena[indeks]}")

# for indeks in range(len(lista_imena)):
#     redni_broj = indeks + 1
#     ime = lista_imena[indeks]
#     print(f"{redni_broj}. {ime}")

# for indeks_ime in enumerate(lista_imena):
#     redni_broj = indeks_ime[0] + 1
#     ime = indeks_ime[1]
#     print(f"{redni_broj}. {ime}")

for indeks, ime in enumerate(lista_imena):
    print(f"{indeks + 1}. {ime}")
