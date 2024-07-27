ime: str = input("Dragi korisnice unesi svoje ime> ")
prezime: str = input("Dragi korisnice unesi svoje prezime> ")
godina_rodenja: int = int(input("Dragi korisnice unesi godinu rodenja> "))
drzava_rodenja: str = input("Dragi korisnice unesi drzavu rodenja> ")
status_radnog_odnosa: str = input("Dragi korisnice unesi (zaposelen/nezaposlen)> ")
jesi_li_zaposlen: bool = bool(input("Dragi korisnice unesi (Da/Ne)> "))
zaposlen: bool = True
tezina_kg: float = float(input("Dragi korisnice unesi masu u kg> "))
spol: str = input("Dragi korisnice unesi spol (M/Z)> ")

print("Ime:",  ime)
print("Prezime:",  prezime)
print("Godina rođenja:",  godina_rodenja)
print("Drzava rođenja:",  drzava_rodenja)
print("Status radnog odnosa:",  status_radnog_odnosa)
print("Tezina:", tezina_kg, "kg")
print("Spol:", spol)

print("\n\n")

print("Ime:",  end=" ")
print(ime)
print("Prezime:", end=" "  )
print(prezime)
print("Godina rođenja:", end=" ")
print(godina_rodenja)
print("Drzava rođenja:",  end=" ")
print(drzava_rodenja)
print("Status radnog odnosa:",  end=" ")
print(status_radnog_odnosa)
print("Tezina:", end=" ")
print(tezina_kg, end=" ")
print("kg")
print("Spol:", end=" ")
print(spol)

ime: str = "Marko"
prezime: str = "Maric"
godina_rodenja: int = 1990
drzava_rodenja: str = "Hravtska"
status_radnog_odnosa: str = "zaposlen"
jesi_li_zaposlen: bool = True
zaposlen: bool = True
tezina_kg: float = 104.5
spol: str = "M"



