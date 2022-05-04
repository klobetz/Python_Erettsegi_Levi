#hozzunk létre egy 10 elemű listát és véletlen számokkal töltsük fel.
#a számok 0 és 100 között generálódjanak

#modulok imprtálása
import random

lista = []
for elemek in enumerate(range(10)):
    r = random.randrange(0,101,1)
    lista.append(r)

print(lista)        # lista kiíratása

print("-"*50)
#egy sorban az egész
list = [random.randrange(0,101,1) for elemek in range(10)]
print(list)
print("-"*50)

#lista eleeinek a kiíratása (bejárás)
for elemek in lista:
    print(elemek, end=", ")

#házi gyakorlás sorbarendezés és fordítva az eeredeti lista nem módosul
# csak a páros számok kiíratása => listáb atétel az elemeknek
#csak a pártlanok kiíratása => listáb atétel az elemeknek
#fibonacci!!!!!!!!