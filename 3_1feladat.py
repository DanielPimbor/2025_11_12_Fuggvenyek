"""3.1 Feladat
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja, 
hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! A program tartalmazza a függvény hívását is! """

szamok_listaja = [1, 2, 3, 4, 6,9,9,12]

def harommal_oszthatok(szamok_listaja):
    oszthato_szamok_szama = 0
    for num in szamok_listaja:
        if num % 3 == 0:
            oszthato_szamok_szama += 1
    return oszthato_szamok_szama

eredmeny = harommal_oszthatok(szamok_listaja)

print(f'A hárommal osztható számok száma:{eredmeny}')