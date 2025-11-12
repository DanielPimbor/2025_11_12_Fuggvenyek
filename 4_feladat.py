"""4. Feladat
Írj egy programot, amelyben van egy 'kerulet' nevű függvény, amely az egyetlen kötelező paramétere mellett fogadhat több paramétert is!
Az opcionális paraméterek száma alapján döntse el milyen síkidomról van szó, és számolja ki a kerületét (0 tetszőleges paraméter: négyzet, 1 tetszőleges paraméter:
téglalap, 2 tetszőleges paraméter: háromszőg, 3 vagy több tetszőleges paraméter: sokszög)!
A program tartalmazzon mindegyik síkidom típusra egy-egy függvényhívást! """



def kerulet(a, *oldal):
    if len(oldal) == 0:
        megoldas = a * 4
    
    elif len(oldal) == 1:
        megoldas = 2*(a + oldal[0])

    elif len(oldal) == 2:
        megoldas = a + oldal[0] + oldal[1]

    else:
        megoldas = sum((a, *oldal))
    return megoldas

"VIGYÁZZ, ne írj cm-ert!!!!"

négyzet=kerulet(10)
print(négyzet)

téglalap=kerulet(10,20)
print(téglalap)

háromszög=kerulet(30,40,50)
print(háromszög)

sokszög=kerulet(10,20,40,30,30,30,40,30,30,30,40)
print(sokszög)