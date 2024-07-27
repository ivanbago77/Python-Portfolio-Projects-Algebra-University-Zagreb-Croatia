moja_prazna_lista = []
print(type(moja_prazna_lista))

moja_prazna_lista_2 = list()
print(type(moja_prazna_lista_2))

moja_raznovrsna_lista = ["Moje ime", 9.8, 10, True, False, True, "Moje ime", 11, 10]
#                           0         1    2   3     4       5      6         7   8
print(moja_raznovrsna_lista)

# iste tipove elemenata
print("\n\n")
lista_voca = ["jabuka", "banana", "tresnja"]
print(lista_voca)

lista_voca.append("kruska")
print("Nakon dodavanja kruske")
print(lista_voca)

# lista_voca.append(6.9)
# print("Nakon dodavanja 6.9")
# print(lista_voca)

print("\n\n")
lista_korsnika = ["Ana", "Marko", "Mate"]
print(lista_korsnika)
lista_korsnika.clear()
print(lista_korsnika)

print("\n\n")
lista_voca.append("kruska")
lista_voca.append("banana")
print(lista_voca)

broj_krusaka = lista_voca.count("kruska")
print(f"Broj krusaka je {broj_krusaka}")

broj_krusaka = lista_voca.count("Kruska")
print(f"Broj krusaka je {broj_krusaka}")

broj_jabuka = lista_voca.count("jabuka")
print(f"Broj jabuka je {broj_jabuka}")

nova_voce_iz_trgovine = ["ribizl", "mandarina"]
lista_voca.extend(nova_voce_iz_trgovine)

print("\n\n")
print("Nakon trgovine")
print(lista_voca)
print(nova_voce_iz_trgovine)

print(lista_voca[5])
print(lista_voca[3])
print(lista_voca[0])

indeks_kruske = lista_voca.index("kruska")
print(f"indeks kruske je {indeks_kruske}")

# indeks_manga = lista_voca.index("mango")
# print(f"indeks manga je {indeks_manga}")

indeks_banane = lista_voca.index("banana")
print(f"indeks banane je {indeks_banane}")

indeks_ribizl = lista_voca.index("ribizl")
print(f"indeks ribizl je {indeks_ribizl}")

print("\n\n")
lista_voca.insert(4, "lubenica")
print(lista_voca)

print(f"Lista voca ima {len(lista_voca)} elemenata")

print("\n\n")
lista_voca.remove("kruska")
print(lista_voca)

# IndexError: list index out of range
# print(f"Voce na indeksu 99 je {lista_voca[99]}")

print("\n\n\n")
print(lista_voca)
varcena_vrijednost = lista_voca.pop(6)
print(f"Element na indeksu 6 je {varcena_vrijednost}")
print(lista_voca)

# print("\n\n\n")
# print(lista_voca)
# varcena_vrijednost = lista_voca.pop(99)
# print(f"Element na indeksu 99 je {varcena_vrijednost}")
# print(lista_voca)


print("\n\n\n")
print(lista_voca)
varcena_vrijednost = lista_voca.pop()
print(f"Element na zadnjem indeks je {varcena_vrijednost}")
print(lista_voca)

# lista_voca.remove(lista_voca[lista_voca.index("banana")])
# lista_voca.remove(lista_voca[1])
# lista_voca.remove("banana")
# # ekvivalent
# lista_voca.pop(1)

print("\n\n\n")
print(lista_voca)
lista_voca.pop(3)
print(lista_voca)

print("\n\n\n")
print(lista_voca)
lista_voca.reverse()
print(lista_voca)

lista_voca.append("Jabuka")
print("\n\n\n")
print(lista_voca)
lista_voca.sort()
print(lista_voca)

print("\n\n\n")
print(lista_voca)
lista_voca.sort(reverse=True)
print(lista_voca)
