stranica_trokuta_a_cm: float = 12.5
visina_na_stranicu_trokuta_a_cm: float = 6.4

povrsina_trokuta_cm2: float = (
    stranica_trokuta_a_cm * visina_na_stranicu_trokuta_a_cm
) / 2

opseg_trokuta_cm: float = stranica_trokuta_a_cm * 3

print(
    "Duljina stranice trokuta iznosi ",
    stranica_trokuta_a_cm,
    " centimetara.",
    sep="",
)

print()

print(
    "Visina stranice trokuta iznosi ",
    visina_na_stranicu_trokuta_a_cm,
    " centimetara.",
    sep="",
    end="\n\n",
)


print(
    "Povrsina trokuta iznosi ",
    povrsina_trokuta_cm2,
    " centimetara kvadratnih.",
    sep="",
    end="\n\n",
)

print(
    "Opseg troguka iznosi ",
    opseg_trokuta_cm,
    " centimetara.",
    sep="",
)
