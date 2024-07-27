moj_string = "Hana"
moj_drugi_str = moj_string

print(id(moj_string))
print(id(moj_drugi_str), end="\n\n")
print(moj_string)
print(moj_drugi_str)

moj_string += "vana"

print(id(moj_string))
print(id(moj_drugi_str), end="\n\n")
print(moj_string)
print(moj_drugi_str)
