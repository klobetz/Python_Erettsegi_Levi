#kiírás fájlba
import random

with open("Kiiratasok/elsokiiras.txt", "w", encoding="utf8") as f:
    f.writelines("Szia Ákos!")

#változó értékének kiírása
szoveg = "Szia Ákos most már változóból!"
with open("Kiiratasok/masodikkiiras.txt", "w", encoding="utf8") as f:
    f.writelines(szoveg)

#felhasználó ad fájlnevet!
#valasz = input("Mi legyen a fájl neve?: ")
valasz = "Teszt1"
with open(f"Kiiratasok/{valasz}.txt", "w", encoding="utf8") as f:
    f.writelines(f"felhasználó álltal {szoveg} megadott fájlnév!!!!!!")

# hozz létre egy 100 elemű listát és töltsd fel véletlen számokkal! (0 és 100 közöttivel)
lista = [random.randrange(0,101,1) for elem in range(100)]

for elem in lista:
    print(elem,end=" ")

print(f"\nA lista {len(lista)} db elemet tartalmat")

#rendezzük növekvőbe a listát:

#rendezett = sorted(lista)
# for elem in renbezett:
#     print(elem,end=" ")

#vagy

for elem in sorted(lista):
    print(elem,end=" ")

#írjuk ki a listát egy fájlba
with open("Kiiratasok/lista.txt", "w", encoding="utf8") as f:
    f.writelines(str(lista))