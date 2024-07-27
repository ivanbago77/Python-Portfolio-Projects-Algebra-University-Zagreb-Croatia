# uzeti od korisnika koliko ljudi zeli
# uzeti imena
# pitati korsinika da odabere jedno ime (pretpostavaka je da to ime postoji)
# ispisati to ime , ime + 3 indeksa, ime + 7 indeksa

# 1.  tezina da smjete prosirivat listu imena koje je korisnik unio
# 2.  tezina da NE smijete prosirivat listu imena koje je korisnik unio

lista_imena = []

broj_ljudi = int(input("Dragi korisncie, koliko ljudi zelis unjeti? "))

for indeks_osobe in range(broj_ljudi):
    nova_osoba = input(f"Dragi korinice daj mi ime {indeks_osobe + 1}. osobe> ")
    lista_imena.append(nova_osoba)

# pretposatvak da je unio ispravno ime
zeljeno_ime = input("Dragi korisnice, odaberi jedno ime koje si unjeo> ")
indeks_zeljenog_imena = lista_imena.index(zeljeno_ime)

# 2. tezina
indeks_plus_3_od_zeljenog_imena = (indeks_zeljenog_imena + 3) % len(lista_imena)
indeks_plus_7_od_zeljenog_imena = (indeks_zeljenog_imena + 7) % len(lista_imena)


ime_za_3_od_zeljenog = lista_imena[indeks_plus_3_od_zeljenog_imena]
ime_za_7_od_zeljenog = lista_imena[indeks_plus_7_od_zeljenog_imena]

print("\n\n")

print(f"Zeljeno ime {zeljeno_ime}")
print(f"Za 3 od zeljenog ime {ime_za_3_od_zeljenog}")
print(f"Za 7 od zeljenog ime {ime_za_7_od_zeljenog}")
