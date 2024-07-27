stranica_cetverokuta_a_cm: float = float(input("Dragi korisnice kolika je duljina stranice cetverokuta a u cm> "))
stranica_cetverokuta_b_cm: float = float(input("Dragi korisnice kolika je duljina stranice cetverokuta b u cm> "))
povrsina_cetverokuta_cm2: float = stranica_cetverokuta_a_cm * stranica_cetverokuta_b_cm

print("\n\n\n")

print("Stranica cetverokuta a:", end=" ")
print(stranica_cetverokuta_a_cm, "cm", sep=" ")
print("Stranica cetverokuta b:", end=" ")
print(stranica_cetverokuta_b_cm, end=" ")
print("cm")
print("Povrsina cetverokuta:", end = " ")
print(stranica_cetverokuta_a_cm, stranica_cetverokuta_b_cm, sep=" + ", end=" ")
print("=", povrsina_cetverokuta_cm2, "cm^2")