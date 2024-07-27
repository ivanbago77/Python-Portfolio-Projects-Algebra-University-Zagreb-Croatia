ime = input("Dragi korisnice unesi svoje ime> ")
prezime = input("Dragi korisnice unesi svoje prezime> ")


print("Puno ime i prezime: {} {}".format(ime, prezime))

adresa = "Matije Gupca 4"
# Mane
# duplanje varijabli ako imam ponavaljanje
# moramo znati tocno tko je na kojoj poziciji tesko je brojat kad ih je vise od 5
# vrijeme gubimo na brojanaje pozicija
print(
    "Puno ime i prezime: {0} {1} \n{0}, Kako si? \nOdakle dolazi  prezime {1}?\n{0} zivi na adresi {2}".format(
        ime, prezime, adresa
    )
)
