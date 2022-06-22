lista =[]

with open("TXT_allomanyok/negyedevesberek.txt",encoding="utf8") as f:
    while True:
        megye = f.readline().strip()
        if not megye:
            break
        elson = int(f.readline().strip().replace(" ",""))   #ez már int
        masodikn = f.readline().strip()                     #ez még string ki kell cserélni a szóközt majd convertálni int-re
        harmadikn = f.readline().strip()
        negyedikn = f.readline().strip()


        adatok = [megye,elson,masodikn,harmadikn,negyedikn]
        lista.append(adatok)

print(f"{lista}")

for elem in lista:
    print(elem[0])
print("-" *50)
#Hány elemet tartalmaz a fájl:
print(f"A Fájl {len(lista)} adatot tartalmaz") #A lista sorait számolja meg jelen esetben ugye 19 sort tartalmaz
print("-" *50)
db = 0
for elem in lista:
    if elem[0]:
        db += 1

print(db)

#Írjuk ki megyénként az első negyedéves béreket formázva úgy hogy egymás alá kerüljenek az adatok:
print("-" *50)
for elem in lista:
    print(f"{elem[0]:25} {elem[1]} Ft")

#melyik megyében a legnagyobb az átlagkereset az eső negyedévben és menyni az!
print("-" *50)
max = 0
for elem in lista:
    if elem[1]>max:
        max = elem[1]

for elem in lista:
    if elem[1]==max:
        print(f"{elem[0]} {max:,} Ft")

#Mennyi volt az országban az első negyedéves átlagbér? Az eredményt két tizedes pontosággal írasd ki!
print("-" *50)

