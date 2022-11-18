tantargyfelosztaslista = []
with open("TXT_allomanyok/beosztas.txt", encoding="utf8") as f:
    while True:
        tanar = f.readline().strip()
        if not tanar:
            break
        tantargy = f.readline().strip()
        osztaly = f.readline().strip()
        oraszam = int(f.readline().strip())
        tantargyfelosztaslista.append([tanar,tantargy,osztaly,oraszam])

print(f"2. feladat\nA fájlban 329 {len(tantargyfelosztaslista)*4} bejegyzés van")

# for tanar,tantargy,osztaly,oraszam in tantargyfelosztaslista:
#     print(tanar)