num1 = int(input("Dame un número: "))
num2 = int(input("Dame otro número: "))

print("while")
while num1 <= num2:
    if num1 % 2 == 0:
        print(num1)
    num1 += 1


