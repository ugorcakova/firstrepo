cislo = int(input("input number"))
vysledok = 0
while cislo != 0:
    zvysok = cislo % 10
    vysledok = vysledok * 10 + zvysok
    cislo = cislo // 10
print(vysledok)