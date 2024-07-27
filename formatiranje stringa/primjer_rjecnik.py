ime = input("Dragi korisnice unesi svoje ime> ")
prezime = input("Dragi korisnice unesi svoje prezime> ")


adresa = "Matije Gupca 4"
# Mane

print(
    "Puno ime i prezime: %(moje_ime)s %(prezime)s \n%(moje_ime)s, Kako si? \nOdakle dolazi  prezime %(prezime)s?\n%(moje_ime)s zivi na adresi %(adresa)s"
    % {"moje_ime": ime, "prezime": prezime, "adresa": adresa}
)
