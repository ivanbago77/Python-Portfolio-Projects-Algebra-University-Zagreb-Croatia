smocnica = ["jabuka", "kruska", "lubenica", "dinja"]
zeli_li_jest = []
je_li_alergican = []
print("Pocetak")

# jedno_voce = smocnica[0]
# for jedno_voce in smocnica:
#     print(jedno_voce)
#     print(f"Trenutno voce je {jedno_voce}")

for jedno_voce in smocnica:
    odgovor_korisnika_zeli_li_jesti = input(
        f"Dragi korisncie, zelis li jesti {jedno_voce}? "
    )
    zeli_li_jest.append(odgovor_korisnika_zeli_li_jesti)
    odgovor_korisnika_je_li_alergican = input(
        f"Dragi korisncie, jesi li alergican na {jedno_voce}? "
    )
    je_li_alergican.append(odgovor_korisnika_je_li_alergican)

for indeks in range(len(smocnica)):
    print(f"{smocnica[indeks]} zeli jesti {zeli_li_jest[indeks]}")

print("Gotovo")
