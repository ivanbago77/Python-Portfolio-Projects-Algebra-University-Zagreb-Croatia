iznos_glavncie_eur = 2000
vremenski_period_godine = 15
godisnja_kamatna_stopa = 2.5 / 100

prinos_u_eur = round(
    iznos_glavncie_eur * vremenski_period_godine * godisnja_kamatna_stopa, 2
)


print("Na ulozenih", iznos_glavncie_eur, "eur", "zaradili smo", prinos_u_eur, "eur")
