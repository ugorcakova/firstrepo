number = int(input("input number"))
backup = number
pocet_cifier = 0
while number != 0:
    pocet_cifier += 1
    number //= 10
# ak je cisel 7, vydelim to 2 == 3 a zvacsim o jedno aby som dostala 4 cislo v poradi (stredne)
if pocet_cifier % 2 == 1:
    index = pocet_cifier // 2 + 1
    neparne = True
else:
    index = pocet_cifier // 2
    neparne = False

pocitadlo_pozicia = 1
while backup != 0:
    cifra = backup % 10
    if neparne:
        if pocitadlo_pozicia == index:
            print(cifra)
    else:
        if pocitadlo_pozicia==index:
            print((cifra + (backup // 10)%10)/2)
    backup //= 10
    pocitadlo_pozicia += 1




