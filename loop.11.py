N = int(input("koniec intervalu:"))
for i in range (1, N + 1):
    if i % 4 == 0 and i % 7 == 0:
        print(i)
