number = int(input("input number"))
backup = number
reversed = 0
while number != 0:
    digit = number % 10
    reversed = reversed*10 + digit
    number //= 10
if backup == reversed:
    print("je symetricke")
else:
    print("nie je symetricke")