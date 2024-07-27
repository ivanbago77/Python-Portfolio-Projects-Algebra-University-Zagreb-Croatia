moj_broj = 1234

print("Moj broj u dekadskom sustavu", moj_broj)
print("Moj broj u binarnom sustavu", bin(moj_broj))
print(type(bin(moj_broj)))
print("Moj broj u oktalni sustavu", oct(moj_broj))
print(type(oct(moj_broj)))
print("Moj broj u heksadekadskom sustavu", hex(moj_broj))
print(type(hex(moj_broj)))

print("\n\n\n")

# int(bin(moj_broj), 2)
# int("0b10011010010", 2)

print("Konverzija nazad iz binarnog", int(bin(moj_broj), 2))
print("Konverzija nazad iz okatlnog", int(oct(moj_broj), 8))
print("Konverzija nazad iz heksadekadskog", int(hex(moj_broj), 16))


moj_broj = 99
moj_broj_bin = bin(moj_broj)
moj_broj_nakon_konverzije_bin_u_dek = int(moj_broj_bin, 2)

print()
print("Orginal", moj_broj)
print("U binarnom sustavu", moj_broj_bin)
print("Nakon konverzije nazad iz bin", moj_broj_nakon_konverzije_bin_u_dek)
