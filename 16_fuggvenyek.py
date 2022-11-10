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

