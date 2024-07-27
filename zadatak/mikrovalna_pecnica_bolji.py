jedan_mjesec_u_danima = int(input("Dragi korisnice koliko trenutni mjesec ima dana> "))
snaga_mikrovalne_pecnice_kw = int(input("Dragi korisnice kolika je snaga mikrovalne pecnice u kW> "))
koristenje_mikrovalne_u_sati_u_danu = int(input("Dragi korisnice koliko sati dnevno koristis mikrovalnu> "))

cijena_struje_u_eur_za_1_kwh = float(input("Dragi korisnice koliko je cijena 1kWh> "))

dnevna_potrosnja_mikrovalne_u_kwh = snaga_mikrovalne_pecnice_kw * koristenje_mikrovalne_u_sati_u_danu

mjesecna_potrosnja_mikrovalne_u_kwh = dnevna_potrosnja_mikrovalne_u_kwh * jedan_mjesec_u_danima

mjesecna_cijena_racuna_za_struju_za_mikrovalnu = mjesecna_potrosnja_mikrovalne_u_kwh * cijena_struje_u_eur_za_1_kwh

print("Racun za jedan mjesec mirkovalne pecnice snage",
      snaga_mikrovalne_pecnice_kw,
      "kW",
      "koja se koristi",
      koristenje_mikrovalne_u_sati_u_danu,
      "h",
      "dnevno iznosi",
      mjesecna_cijena_racuna_za_struju_za_mikrovalnu,
      "eur")

print("\n\n\n")