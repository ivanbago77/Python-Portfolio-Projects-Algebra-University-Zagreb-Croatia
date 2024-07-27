ip_addresa_dio_1 = 192
ip_addresa_dio_2 = 168
ip_addresa_dio_3 = 0
ip_addresa_dio_4 = 184

print("Orginalan IP adresa")
print(
    ip_addresa_dio_1,
    ip_addresa_dio_2,
    ip_addresa_dio_3,
    ip_addresa_dio_4,
    sep=".",
    end="\n\n",
)


print("BIN IP adresa")
print(
    bin(ip_addresa_dio_1)[2:],
    bin(ip_addresa_dio_2)[2:],
    bin(ip_addresa_dio_3)[2:],
    bin(ip_addresa_dio_4)[2:],
    sep=".",
    end="\n\n",
)


print("OCT IP adresa")
print(
    oct(ip_addresa_dio_1)[2:],
    oct(ip_addresa_dio_2)[2:],
    oct(ip_addresa_dio_3)[2:],
    oct(ip_addresa_dio_4)[2:],
    sep=".",
    end="\n\n",
)

print("OCT IP adresa")
print(
    hex(ip_addresa_dio_1)[2:],
    hex(ip_addresa_dio_2)[2:],
    hex(ip_addresa_dio_3)[2:],
    hex(ip_addresa_dio_4)[2:],
    sep=".",
    end="\n\n",
)
