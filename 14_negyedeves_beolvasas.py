lista =[]

with open("TXT_allomanyok/negyedevesberek.txt",encoding="utf8") as f:
    while True:
        megye = f.readline().strip()
        if not megye:
            break
        elson = f.readline().strip()
        masodikn = f.readline().strip()
        harmadikn = f.readline().strip()
        negyedikn = f.readline().strip()


        adatok = [megye,elson,masodikn,harmadikn,negyedikn]
        lista.append(adatok)


for elem in lista:
    print(elem[0])