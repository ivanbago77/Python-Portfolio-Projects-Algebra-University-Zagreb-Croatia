crvena = int(input("Dragi korisnice upisi crvenu komponentu > "))
zelena = int(input("Dragi korisnice upisi zelenu komponentu > "))
plava = int(input("Dragi korisnice upisi plavu komponentu > "))

print("RGB")
print(crvena, zelena, plava, sep=", ", end="\n\n\n")

print("HEX")
print("#", end="")
print(hex(crvena), hex(zelena), hex(plava), sep=", ", end="\n\n\n")

print("HEX")
print("#", end="")
print(hex(crvena)[:2].zfill(2), hex(zelena)[:2].zfill(2), hex(plava)[:2].zfill(2), sep="", end="\n\n\n")