# z prava do lava
cislo = int(input("input number"))
vysledok_parne = 0
vysledok_neparne = 0
while cislo != 0:
    zvysok = cislo % 10
    if zvysok % 2 == 0:
        vysledok_parne = vysledok_parne * 10 + zvysok
    if zvysok % 2 == 1:
        vysledok_neparne = vysledok_neparne * 10 + zvysok
    cislo = cislo // 10
print(vysledok_parne, vysledok_neparne)

# z lava do prava
cislo = int(input("input number"))
vysledok_parne = " "
vysledok_neparne = " "

while cislo != 0:
    zvysok = cislo % 10
    if zvysok % 2 == 0:
        vysledok_parne = str(zvysok) + vysledok_parne
    if zvysok % 2 == 1:
        vysledok_neparne = str(zvysok) + vysledok_neparne
    cislo = cislo // 10
print(vysledok_parne, vysledok_neparne)
