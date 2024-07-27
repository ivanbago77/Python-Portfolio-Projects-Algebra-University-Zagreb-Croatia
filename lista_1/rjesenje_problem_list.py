voce = ["jabuka", "kruska", "sljiva", "lubencia", "dinja", "ribizl", "papaja"]

for vocka in voce:
    print(f"{voce.index(vocka) + 1}. rangirano voce je {vocka}")

# print(f"1. rangirano voce je {voce[0]}")
# print(f"2. rangirano voce je {voce[1]}")
# print(f"3. rangirano voce je {voce[2]}")
# print(f"4. rangirano voce je {voce[3]}")
# print(f"5. rangirano voce je {voce[4]}")

# print(f"X. rangirano voce je {voce[X]}")

place_radnika = [1000.0, 1010.0, 1500, 900, 666, 777]

# place_radnika[0] = place_radnika[0] + 200.0
# place_radnika[1] = place_radnika[1] + 200.0
# place_radnika[2] = place_radnika[2] + 200.0
# place_radnika[3] = place_radnika[3] + 200.0

for placa_radnika in place_radnika:
    place_radnika[place_radnika.index(placa_radnika)] = placa_radnika + 200.0

# place_radnika[X] = place_radnika[X] + 200.0

print("Place nakon povecanja su")
print(place_radnika)
