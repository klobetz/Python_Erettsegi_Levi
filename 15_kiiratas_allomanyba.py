#kiírás fájlba
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