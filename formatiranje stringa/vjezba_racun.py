# | Naziv proizvoda | Kolicina | Cijena 1 kom | PDV  | Ukupna cijena |
# odaberite 3 proizvoda i ispsite u obliku racuna

poravananje = 20

horizontalni_razmak = "-" * poravananje
horizonrtalni_odjeljak = (
    "+"
    + horizontalni_razmak
    + "+"
    + horizontalni_razmak
    + "+"
    + horizontalni_razmak
    + "+"
    + horizontalni_razmak
    + "+"
    + horizontalni_razmak
    + "+"
)

stil_naziv_proizvoda = f"<{poravananje}s"
stil_kolicina_proizvoda = f"^{poravananje}d"
stil_cijena = f">{poravananje}.2f"
stil_pdv = f">{poravananje}d"
stil_naziv_kolone = f"^{poravananje}s"

print(horizonrtalni_odjeljak)
print(
    f"|{'Naziv proizvoda':{stil_naziv_kolone}}|{'Kolicina':{stil_naziv_kolone}}|{'Cijena 1 kom (EUR)':{stil_naziv_kolone}}|{'PDV (%)':{stil_naziv_kolone}}|{'Ukupna cijena (EUR)':{stil_naziv_kolone}}|"
)
print(horizonrtalni_odjeljak)
print(
    f"|{'WC papir':{stil_naziv_proizvoda}}|{10:{stil_kolicina_proizvoda}}|{2.4:{stil_cijena}}|{25:{stil_pdv}}|{24.0:{stil_cijena}}|"
)
print(horizonrtalni_odjeljak)
print(
    f"|{'Paprika':{stil_naziv_proizvoda}}|{1234:{stil_kolicina_proizvoda}}|{1.4:{stil_cijena}}|{20:{stil_pdv}}|{1224.0:{stil_cijena}}|"
)
print(horizonrtalni_odjeljak)
print(
    f"|{'Sladoled':{stil_naziv_proizvoda}}|{3:{stil_kolicina_proizvoda}}|{12.4:{stil_cijena}}|{25:{stil_pdv}}|{2224.0:{stil_cijena}}|"
)
print(horizonrtalni_odjeljak)
