#függvény írása
import datetime


def osszead():
    print(5+4)
#függvény meghívása
osszead()

#visszatérési érték (return)
def osszead2():
    a = 10
    b = 15
    #c = a+b
    #return c        #visszatérési érték
    return a+b
print(osszead2())

#parméter használata a függvényben, illetve paraméter átadás
#szorzás függvény paramétereivel:
def sorzas(a,b):        #paraméter létrehozása
    return a*b          #visszatérési érték

print(sorzas(5.6,8))      #paraméter átadása a függvénynek

#Írj egy Python eljárást, amely paraméterként kap 2 egész számot (N és M) és kiír a képernyőre a csillag (*)
#karaktereket M darab sorban és N darab oszlopban (tehát NxM darab karaktert egy téglalap alakú képernyőrészre)!
#A programodban hívd is meg ezt az alprogramot!

#x,y = int(input("kérek egy számot: ")),int(input("kérek egy másikszámot: "))
def feladat(n,m):
    for i in range(m):
        print("*"*n)

feladat(int(input("oszlop: ")),int(input("sor: ")))
#feladat(x,y)

#Írj egy logikai értékkel visszatérő Python függvényt, amely paraméterként kap egy egész számot és
#eldönti a számról, hogy osztható-e 2-vel és 3-mal is egyszerre! A programodban hívd is meg ezt az alprogramot!
#péter gábor
def oszthato(x):
    if x%2==0 and x%3==0:
        return True


if oszthato(int(input("Kérek egy számot: "))) == True:
    print("igen osztható")
else:
    print("nem osztható")