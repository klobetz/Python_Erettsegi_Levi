nevek = []
with open("TXT_allomanyok/nevek.txt",encoding="utf8") as f:
    fejlec = f.readline()
    for adat in f:
        sor = adat.strip().split()
        vnev = sor[0]
        knev = sor[1]
        if len(sor)>2:
            knev2 = sor[2]
            adatok = [vnev, knev, knev2]
            nevek.append(adatok)
        else:
            adatok=[vnev , knev]
            nevek.append(adatok)

print(nevek)

print(f"A lista hossza: {len(nevek)}")

for elem in nevek:
    if len(elem) > 2:
        print(f"{elem[0]} {elem[1]} {elem[2]}")