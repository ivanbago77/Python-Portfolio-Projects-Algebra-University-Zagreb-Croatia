jedan_mjesec_u_danima = 30
snaga_mikrovalne_pecnice_u_kw = 1.3
koristenje_mikrovalne_u_sati_u_danu = 2

cijena_struje_u_eur_za_1_kwh = 0.11

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
