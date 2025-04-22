# Reverse the order of digits in the integer N.
N = int(input("Enter a Number : "))
rev_number = 0
while N > 0:
    last_digit =  N % 10
    rev_number = (rev_number * 10) + last_digit
    N = N // 10

print("Reversed Number :", rev_number)