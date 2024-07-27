glavni_gradovi = ["Pariz", "Zagreb", "Berlin", "Madrid", "rim", "Rim"]


sortirana_listu_gradova = sorted(
    glavni_gradovi, key=lambda ime_grada: (len(ime_grada), ime_grada)
)
print(glavni_gradovi)
print(sortirana_listu_gradova)
