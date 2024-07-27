# uzeti ime, prezime, godian rodenja, status_zaposlenosti i masa
# |Ime     |   Marko   |
# |Prezime |      |
# ...
ime = input("Dragi korisnicec, unesite vase ime> ")
prezime = input(f"Dragi {ime}, unesite vase prezime> ")
godina_rodenja = int(input(f"Dragi {ime}, kad ste rodeni> "))
status_zaposlenosti = input(f"Dragi {ime}, jeste li zapsoleni> ")
masa_kg = float(input(f"Dragi {ime}, koliko imate kg> "))

poravanje = 20

horizontalni_odjeljak = "-" * poravanje
tablica_horizontalno = "+" + horizontalni_odjeljak + "+" + horizontalni_odjeljak + "+"

print(tablica_horizontalno)
print(f"|{'Ime':<{poravanje}s}|{ime.title():^{poravanje}s}|")
print(tablica_horizontalno)
print(f"|{'Prezime':<{poravanje}s}|{prezime.title():^{poravanje}s}|")
print(tablica_horizontalno)
print(f"|{'Godina rodenja':<{poravanje}s}|{godina_rodenja:^{poravanje}}|")
print(tablica_horizontalno)
print(f"|{'Zaposlen':<{poravanje}s}|{status_zaposlenosti:^{poravanje}}|")
print(tablica_horizontalno)
print(f"|{'Masa (kg)':<{poravanje}s}|{masa_kg:^{poravanje}.0f}|")
print(tablica_horizontalno)
