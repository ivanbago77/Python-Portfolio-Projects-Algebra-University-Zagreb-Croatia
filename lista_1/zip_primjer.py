drzave = ["Francuska", "Hrvatska", "Njemacka", "Spanjolska"]
glavni_gradovi = ["Pariz", "Zagreb", "Berlin", "Madrid"]
broj_stanovnika_gl_gradovi = [10_000_000, 1_000_000, 8_000_000, 7_000_000]

for drzava, glavni_grad, broj_stanovnika_gl_grad in zip(
    drzave, glavni_gradovi, broj_stanovnika_gl_gradovi
):
    print(
        f"Glavni grad {glavni_grad} drzave {drzava} ima {broj_stanovnika_gl_grad:,.0f} ljudi."
    )
