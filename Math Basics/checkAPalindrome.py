# Determine whether a given integer is a palindrome or not.

N = int(input("Enter a number : "))
M = N
rev_num = 0
while N > 0:
    last_digit = N % 10
    rev_num = (rev_num * 10) + last_digit
    N = N // 10

if rev_num == M:
    print("The given number is a Palindrome")
else:
    print("The given number is not a Palindrome")