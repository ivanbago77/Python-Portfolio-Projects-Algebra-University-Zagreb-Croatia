print("\n\n 2. nacin")

moja_lista_imena = ["Marko", "Ivan", "Hana"]
moja_lista_mix = [1, moja_lista_imena, 9.99, True]

print("Orginalna lista", moja_lista_mix)

moja_lista_mix_kopirana = moja_lista_mix[:]

print("Moaj lista kopirana", moja_lista_mix_kopirana)

moja_lista_mix[2] = "Halo tamo"

# moja_lista_imena[0] = "Vana"
# moja_lista_imena[2] = "Andrija"

moja_lista_mix[1][0] = "Vana"
moja_lista_mix[1][2] = "Andrija"

print("\n\n")
print(moja_lista_imena)
print(moja_lista_mix)
print(moja_lista_mix_kopirana)
