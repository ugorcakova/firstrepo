# loops 7 - kazde cislo delitelne 3
N = int(input("koniec intervalu:"))
for i in range (1, N + 1):
    if i % 3 == 0:
        print(i)