#kiírás fájlba
with open("Kiiratasok/elsokiiras.txt", "w", encoding="utf8") as f:
    f.writelines("Szia Ákos!")

#változó értékének kiírása
szoveg = "Szia Ákos most már változóból!"
with open("Kiiratasok/masodikkiiras.txt", "w", encoding="utf8") as f:
    f.writelines(szoveg)