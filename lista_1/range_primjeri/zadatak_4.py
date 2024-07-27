lista_imena = []

broj_ljudi = int(input("Dragi korisncie, koliko ljudi zelis unjeti? "))

for indeks_osobe in range(broj_ljudi):
    nova_osoba = input(f"Dragi korinice daj mi ime {indeks_osobe + 1}. osobe> ")
    lista_imena.append(nova_osoba)

broj_timova = int(input("Dragi korisnice, na koliko timova zelis da podijelim ljude> "))
redni_broj_tima_1 = 0
redni_broj_tima_2 = 1

# pitati korisnika koliko timova hoce i ispisati timove na ekranu

print("Tim 1:")
for indeks in range(redni_broj_tima_1, len(lista_imena), broj_timova):
    print(f"\t{lista_imena[indeks]}")

print("\n\n")
print("Tim 2:")
for indeks in range(redni_broj_tima_2, len(lista_imena), broj_timova):
    print(f"\t{lista_imena[indeks]}")
