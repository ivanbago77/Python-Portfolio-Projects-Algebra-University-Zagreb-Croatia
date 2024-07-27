glavni_gradovi = ["Pariz", "Zagreb", "Berlin", "Madrid", "rim", "Rim"]

# glavni_gradovi.sort()

# print("Glavni gradovi soretirani abecedno su:")
# print(glavni_gradovi)

# glavni_gradovi.sort(key=lambda ime_grada: len(ime_grada))
# print(glavni_gradovi)

glavni_gradovi.sort(key=lambda ime_grada: (len(ime_grada), ime_grada), reverse=True)
print(glavni_gradovi)
