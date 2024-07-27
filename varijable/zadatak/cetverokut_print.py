stranica_cetverokuta_a_cm: float = 2.5
stranica_cetverokuta_b_cm: float = 4.5
povrsina_cetverokuta_cm2: float = stranica_cetverokuta_a_cm * stranica_cetverokuta_b_cm

print("Stranica cetverokuta a:", stranica_cetverokuta_a_cm, "cm")
print("Stranica cetverokuta b:", stranica_cetverokuta_b_cm, "cm")
print("Povrsina cetverokuta:", stranica_cetverokuta_a_cm, "cm", "+", stranica_cetverokuta_b_cm, "cm", "=", povrsina_cetverokuta_cm2, "cm^2")

print("\n\n\n")

print("Stranica cetverokuta a:", end=" ")
print(stranica_cetverokuta_a_cm, "cm", sep=" ")
print("Stranica cetverokuta b:", end=" ")
print(stranica_cetverokuta_b_cm, end=" ")
print("cm")
print("Povrsina cetverokuta:", end = " ")
print(stranica_cetverokuta_a_cm, stranica_cetverokuta_b_cm, sep=" + ", end=" ")
print("=", povrsina_cetverokuta_cm2, "cm^2")
