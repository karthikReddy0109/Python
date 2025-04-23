# Find GCD / HCF of two numbers:
a = int(input("Enter value for a : "))
b = int(input("Enter value for b : "))

while a != 0 and b != 0:
    if a >= b:
        a = a % b 
    else:
        b = b % a

    print("a =", a)
    print("b =", b)
if a == 0:
    print("GCD is :", b)
else:
    print("GCD is : ", a)