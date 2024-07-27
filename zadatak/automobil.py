# TODO: probaj naci kraci naziv
potrosnja_automobila_na_100_km_u_l = 5.3
cijena_goriva_u_eur_za_1_l = 1.2

potrosnja_automobila_na_1_km_u_l = potrosnja_automobila_na_100_km_u_l / 100

cijena_1_km_voznje_u_eur = potrosnja_automobila_na_1_km_u_l * cijena_goriva_u_eur_za_1_l
cijena_1_km_voznje_u_eur = round(cijena_1_km_voznje_u_eur, 2)

print("Cijena jednog km voznje iznosi", cijena_1_km_voznje_u_eur, "eur")

dnevna_voznja_do_posla_km = 20
dnevna_voznja_do_posla_i_nazad_km = 2 * dnevna_voznja_do_posla_km
broj_dana_u_mjesecu = 30

mjesecna_udaljenost_do_posla_i_nazad_u_km = (
    broj_dana_u_mjesecu * dnevna_voznja_do_posla_i_nazad_km
)

mjesecna_cijena_voznje_do_posla_i_nazad_u_eur = (
    mjesecna_udaljenost_do_posla_i_nazad_u_km * cijena_1_km_voznje_u_eur
)

mjesecna_cijena_voznje_do_posla_i_nazad_u_eur = round(
    mjesecna_cijena_voznje_do_posla_i_nazad_u_eur, 2
)

print(
    "Mjesecna cijena coznje do posal i nazad je",
    mjesecna_cijena_voznje_do_posla_i_nazad_u_eur,
    "eur",
)
