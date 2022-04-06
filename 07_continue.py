#continue => vezérlés átadó utasítás a, ciklustörzs további része nem fut le viszont a program folytetódik tovább

lista=[2,6,12,15,18,19,21,24,25,34,39,50]

for paros in lista:
    if paros % 2==0:
        print(paros)

for i in lista:
    if i % 2 ==1:
        break
    print(i, end=' ')

print()

for i in lista:
    if i % 2 ==1:
        continue
    print(i, end=' ')