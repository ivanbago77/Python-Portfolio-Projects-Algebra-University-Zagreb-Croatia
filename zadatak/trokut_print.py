stranica_trokuta_a_cm = float(input("Dragi korisnice unesi duljinu stranice trokuta tako a u cm"))
stranica_trokuta_b_cm = float(input("Dragi korisnice unesi duljinu stranice trokuta tako b u cm"))
stranica_trokuta_c_cm = float(input("Dragi korisnice unesi duljinu stranice trokuta tako c u cm"))
visina_trokuta_na_stranicu_a_cm = float(input("Dragi korisnice unesi duljinu visine na stranicu trokuta a u cm"))

opseg_trokuta_cm = stranica_trokuta_a_cm + stranica_trokuta_b_cm + stranica_trokuta_c_cm
povrsina_trokuta_cm2 = (stranica_trokuta_a_cm * visina_trokuta_na_stranicu_a_cm) / 2 

print("Stranica trokuta a je", stranica_trokuta_a_cm, "cm")
print("Stranica trokuta b je", stranica_trokuta_b_cm, "cm")
print("Stranica trokuta c je", stranica_trokuta_c_cm, "cm")
print("Visina na stranicu a trokuta je", visina_trokuta_na_stranicu_a_cm, "cm")

print("Povrsina trokuta:")
print("(", visina_trokuta_na_stranicu_a_cm , "*", stranica_trokuta_a_cm, ")", "/2", povrsina_trokuta_cm2, "cm^2")
print("Opseg trokuta je:", stranica_trokuta_a_cm, "+" , stranica_trokuta_b_cm, "+" , stranica_trokuta_c_cm, "=", opseg_trokuta_cm, "cm")

print("Povrsina trokuta:")
print("(", visina_trokuta_na_stranicu_a_cm , "*", stranica_trokuta_a_cm, ")")
print("--------------", "=", povrsina_trokuta_cm2, "cm^2")
print("      2     ")