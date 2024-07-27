znak_x = "X"
znak_o = "O"

poravnanje = 5
stil = f"^{poravnanje}s"

horizontalni_odjeljak = "-" * poravnanje

horizontalni_separator = (
    "+"
    + horizontalni_odjeljak
    + "+"
    + horizontalni_odjeljak
    + "+"
    + horizontalni_odjeljak
    + "+"
)

print(horizontalni_separator)
print(f"|{' ':{stil}}|{znak_o:{stil}}|{znak_x:{stil}}|")
print(horizontalni_separator)
print(f"|{' ':{stil}}|{' ':{stil}}|{znak_o:{stil}}|")
print(horizontalni_separator)
print(f"|{znak_x:{stil}}|{znak_o:{stil}}|{znak_x:{stil}}|")
print(horizontalni_separator)
