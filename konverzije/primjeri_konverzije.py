moj_prvi_broj = int("64")

print(type(moj_prvi_broj))
print(moj_prvi_broj)


# ValueError: invalid literal for int() with base 10: '64.6'
# moj_drugi_broj = int("64.6")

# print(type(moj_drugi_broj))
# print(moj_drugi_broj)

# ValueError: invalid literal for int() with base 10: 'Marko'
# int_txt = int("Marko")

# print(type(int_txt))
# print(int_txt)

int_bool = int(True)

print(type(int_bool))
print(int_bool)


moj_prvi_decimalni_broj = float("6.4")
print(type(moj_prvi_decimalni_broj))
print(moj_prvi_decimalni_broj)

moj_prvi_decimalni_broj = float("6")
print(type(moj_prvi_decimalni_broj))
print(moj_prvi_decimalni_broj)


moj_prvi_decimalni_broj = float(True)
print(type(moj_prvi_decimalni_broj))
print(moj_prvi_decimalni_broj)

# ValueError: could not convert string to float: 'Broj'
# moj_prvi_decimalni_broj = float("Broj")
# print(type(moj_prvi_decimalni_broj))
# print(moj_prvi_decimalni_broj)

moj_prvi_boolean = bool("True")
print(type(moj_prvi_boolean))
print(moj_prvi_boolean)

moj_prvi_boolean = bool("False")
print(type(moj_prvi_boolean))
print(moj_prvi_boolean)

print("\n\n\n")
print(bool(""))
print(bool(None))
print(bool(0))
print(bool([]))
print(bool(0.0))
print(bool(False))

print("\n\n\n")
print(bool("False"))
print(bool(9.9))
print(bool(0.001))
print(bool(["ante"]))
print(bool(True))

print("\n\n\n")
print(chr(65))
print(chr(52))
print(chr(121))

print("\n\n\n")
print(ord("A"))
print(ord("4"))
print(ord("y"))
