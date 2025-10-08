z = int(input("zaciatok intervalu:"))
k = int(input("koniec intervalu:"))
pocet = 0
for i in range (z, k+1):
    if i % 8 == 0:
        pocet += 1
print (pocet)