ip_adresa_dio_1 = 192
ip_adresa_dio_2 = 168
ip_adresa_dio_3 = 0
ip_adresa_dio_4 = 184

print("Originalna IP adresa")
print(
    ip_adresa_dio_1, 
    ip_adresa_dio_2, 
    ip_adresa_dio_3, 
    ip_adresa_dio_4, 
    sep = ".", 
    end="\n\n"
    )

print("BIN IP adresa")
print(
    bin(ip_adresa_dio_1), 
    bin(ip_adresa_dio_2), 
    bion(ip_adresa_dio_3), 
    bin(ip_adresa_dio_4), 
    sep = ".", 
    end="\n\n"
    )

print("OCT IP adresa")
print(
    oct(ip_adresa_dio_1), 
    oct(ip_adresa_dio_2), 
    oct(ip_adresa_dio_3), 
    oct(ip_adresa_dio_4), 
    sep = ".", 
    end="\n\n"
    )

print("HEX IP adresa")
print(
    hex(ip_adresa_dio_1), 
    hex(ip_adresa_dio_2), 
    hex(ip_adresa_dio_3), 
    hex(ip_adresa_dio_4), 
    sep = ".", 
    end="\n\n"
    )