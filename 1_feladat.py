"""1. Feladat
Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt, ami a paraméterként átvett listaelemeket (egész számokat) 
összeadja és az összegükkel tér vissza! A program tartalmazza a függvény hívását is! """

szamok_listaja = [1, 2, 3, 4, 5]

def osszegzo(szamok):
    sum = 0
    for szam in szamok:
        sum += szam
    return sum

eredmeny = osszegzo(szamok_listaja)
print(eredmeny)