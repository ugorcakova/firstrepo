# loops 5 - odmocnina zaokruhlena na 2
Z = int(input("zaciatok funkcie:"))
K = int(input("koniec funkcie:"))
for i in range (Z, K+1):
    print (i, round(i**0.5, 2))