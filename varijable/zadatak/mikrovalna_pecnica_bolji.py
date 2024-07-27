jedan_mjesec_u_danima = int(input("Dragi korisnice koliko trenutni mjesec ima dana> "))
snaga_mikrovalne_pecnice_u_kw = int(
    input("Dragi korisnice kolika je snaga mikrovalne pecnice u kW> ")
)
koristenje_mikrovalne_u_sati_u_danu = int(
    input("Dragi korisnice koliko sati dnevno koristis mikorvalnu> ")
)

cijena_struje_u_eur_za_1_kwh = float(input("Dragi korisnice koliko ciejna 1kWh> "))

dnevna_potrosnja_mikrovalne_u_kwh = (
    snaga_mikrovalne_pecnice_u_kw * koristenje_mikrovalne_u_sati_u_danu
)

mjesecna_potrosnja_mikrovalne_u_kwh = (
    dnevna_potrosnja_mikrovalne_u_kwh * jedan_mjesec_u_danima
)

mjesecna_cijena_racuna_za_struju_za_mirkovalnu = (
    mjesecna_potrosnja_mikrovalne_u_kwh * cijena_struje_u_eur_za_1_kwh
)

print(
    "Racun za jedna mjesec mikrovalne pecnice snage",
    snaga_mikrovalne_pecnice_u_kw,
    "kW",
    "koja se koristi",
    koristenje_mikrovalne_u_sati_u_danu,
    "h",
    "dnevno iznosi",
    mjesecna_cijena_racuna_za_struju_za_mirkovalnu,
    "eur",
)

print("\n\n\n")
