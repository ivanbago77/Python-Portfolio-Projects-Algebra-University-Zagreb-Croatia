stranica_cetverokuta_a_cm: float = float(
    input("Dragi korisncie kolika je duljina strance cetverokuta a u cm> ")
)
stranica_cetverokuta_b_cm: float = float(
    input("Dragi korisncie kolika je duljina strance cetverokuta b u cm> ")
)
povrsina_cetverokuta_cm2: float = stranica_cetverokuta_a_cm * stranica_cetverokuta_b_cm

print("Stranica cetverokuta a:", stranica_cetverokuta_a_cm, "cm")
print("Stranica cetverokuta b:", stranica_cetverokuta_b_cm, "cm")
print(
    "Povrsina cetverokuta:",
    stranica_cetverokuta_a_cm,
    "cm",
    "+",
    stranica_cetverokuta_b_cm,
    "cm",
    "=",
    povrsina_cetverokuta_cm2,
    "cm^2",
)
