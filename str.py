number = int(input("input number"))
reversed = 0
while number != 0:
    digit = number % 10
    reversed *= 10 + digit
    number //= 10
if number == reversed:
    print("je symetricke")
else:
    print ("nie je symetricke")