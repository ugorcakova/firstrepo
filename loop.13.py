N = int(input("koniec intervalu:"))
sucet = 0
for i in range (1, N + 1):
    if i % 2 == 0:
        sucet += i
print("sucet je:", sucet)