# Pitajte korisnika ime filma
# tko je redatelj
# koja godina
# koja je ocijena filma na IMDB
# lijepo ispiste sve na ekran svaki podatak u zaseban red koristeci .format
# f string

ime_filma = input("Dragi korisnice, unesi ime filma> ")
redatelj = input(f"Tko je redatelj {ime_filma}> ")
godina = int(input(f"Koje godine je film {ime_filma} izasao> "))
ocijena = float(input(f"Koja je prosjecna ocijena filma {ime_filma}> "))

print(end="\n\n\n")

print(f"Film: {ime_filma}")
print(f"Redatelj: {redatelj}")
print(f"Godina izlaska: {godina}")
print(f"Ocijena: {ocijena}")

print(end="\n\n\n")

print("Film: {}".format(ime_filma))
print("Redatelj: {}".format(redatelj))
print("Godina izlaska: {}".format(godina))
print("Ocijena: {}".format(ocijena))
