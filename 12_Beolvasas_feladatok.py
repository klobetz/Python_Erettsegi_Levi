#beolvasás
list = []
with open("TXT_allomanyok/autok.txt", encoding="utf8") as f:
    for adat in f:
        sor = adat.strip().split()

        nap = int(sor[0])
        ido = sor[1]
        rendszam = sor[2]
        azonosito = sor[3]
        km = sor[4]
        kibehajtas = sor[5]
        adatok=[nap,ido,rendszam,azonosito,km,kibehajtas]
        list.append(adatok)

print(list)
for elem in list:
    print(elem[0])