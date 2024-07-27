stranica_trokuta_a_cm = float(
    input("Dragi korisnice unesi duljinu stranice trokuta a u cm> ")
)
stranica_trokuta_b_cm = float(
    input("Dragi korisnice unesi duljinu stranice trokuta b u cm> ")
)
stranica_trokuta_c_cm = float(
    input("Dragi korisnice unesi duljinu stranice trokuta c u cm> ")
)
visina_na_stranicu_a_cm = float(
    input("Dragi korisnice unesi duljinu visine na stranicu trokuta a u cm> ")
)

povrsina_trokuta_u_cm2 = (stranica_trokuta_a_cm * visina_na_stranicu_a_cm) / 2
opseg_trokuta_cm = stranica_trokuta_a_cm + stranica_trokuta_b_cm + stranica_trokuta_c_cm

print("Stranica trokuta a je", stranica_trokuta_a_cm, "cm")
print("Stranica trokuta b je", stranica_trokuta_b_cm, "cm")
print("Stranica trokuta c je", stranica_trokuta_c_cm, "cm")
print("Visina na stranicu a je", visina_na_stranicu_a_cm, "cm")
print(
    "Povrsina trokuta:",
    "(",
    visina_na_stranicu_a_cm,
    "*",
    stranica_trokuta_a_cm,
    ")",
    "/ 2",
    "=",
    povrsina_trokuta_u_cm2,
    "cm^2",
)
print(
    "Opseg trokuta:",
    stranica_trokuta_a_cm,
    "+",
    stranica_trokuta_b_cm,
    "+",
    stranica_trokuta_c_cm,
    "=",
    opseg_trokuta_cm,
    "cm",
)
print("Povrsina trokuta:")
print("(", visina_na_stranicu_a_cm, "*", stranica_trokuta_a_cm, ")")
print("--------------", " = ", povrsina_trokuta_u_cm2, "cm^2")
print("      2       ")
