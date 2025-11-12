"""2. Feladat
Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt, amely True értékkel tér vissza, ha a paraméterként átvett listaelemek (egész számok) között van páros, 
ellenkező esetben a visszatérési érték False! A program tartalmazza a függvény hívását is! """

szamok_listaja = [1, 2, 3, 4, 5]

def paros_e(szamok_listaja):
    for num in szamok_listaja:
        if num % 2 == 0:
            return True
    return False

eredmeny = paros_e(szamok_listaja)
print(eredmeny)