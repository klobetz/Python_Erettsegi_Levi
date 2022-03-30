#adat bekérés
input("Kérek egy valamit: ")
print("Köszönöm!")

#letárolása a váasznak egy VÁLTOZÓBA!!!!!!
valasz = input("Kérek egy valamit: ")
print(f"Köszönöm! a válaszod a kérdésre: {valasz}")

#kört sugarát bekérjük és a terület kiszámítása terület => r2*PI
sugar = float(input("Kérem adja meg a kör sugarát: "))
terulet = sugar**2*3.14159  #sugar*sugar*3.14159
print(f"A kör területe: {terulet}")

#vagy

sugar2 = float(input("Kérem adja meg a kör sugarát2: "))
print(f"A kör területe: {sugar2**2*3.14159}")

#vagy

print(print("A kör területe:", float(input("Kérem adja meg a kör sugarát3: "))**2*3.14159))


#a megadott érték ellenőrzése
try:
    valasz_szam = int(input("Kérek egy egész számot: "))
except ValueError:
    print("Nem számot adtál meg!!!!")

# addig ne engedjen tovább amíg az nem szám!!!
while True:
    try:
        valasz_szam2 = int(input("Kérek egy egész számot: "))
    except ValueError:
        print("Nem számot adtál meg!!!!")
    else:
        print(f"Köszönöm!!! Az értéket eltároltam! a megadott érték: {valasz_szam2}")
        break


#sztring vizsgálata
valasz_szam3 = input("Kérem a nevedet: ")
print(valasz_szam3.isdigit())               #bool típust kapok vissza amit while-al már tudok vizsgálni!

valasz_szam3 = input("Kérem a nevedet: ")
while valasz_szam3.isdigit() == True or valasz_szam3 == " ":
    valasz_szam3 = input("Nem a nevedet kaptem meg!!!\nAdd meg a nevedet: ")
print(f"Köszönöm a beírt név: {valasz_szam3}")

#vagy a szám vizsgálata
valasz_szam4 = input("Kérek egy számot: ")
while valasz_szam4.isdigit() != True:
    valasz_szam4 = input("Nem számot adtál meg!!!!\nAdd meg a számot: ")
print(f"Köszönöm a beírt szám: {valasz_szam4}")