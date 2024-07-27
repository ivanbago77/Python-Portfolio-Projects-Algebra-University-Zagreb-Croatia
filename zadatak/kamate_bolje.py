iznos_glavnice_eur = float(input("Dragi korisnice koliko iznosi glavnica u eur> "))
vremenski_period_godine = int(input("Dragi korisnice na koliko godina> "))
godisnja_kamatna_stopa = float(input("Dragi korisnice kolika je kamatna stopa(%)> ")) / 100


prinos_u_eur = round(
    iznos_glavnice_eur * vremenski_period_godine * godisnja_kamatna_stopa, 2
    )

print("Na ulozenih", iznos_glavnice_eur, "eur", "zaradili smo", prinos_u_eur, "eur")
