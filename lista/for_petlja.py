smocnica = ["jabuka", "kruska", "lubencia", "dinja"]
zeli_li_jest = []
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

print(smocnica)
print(zeli_li_jest)

print("Gotovo")
