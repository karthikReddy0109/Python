# Write a program that reads an integer from the standard input and then prints each digit of the number on a new line in reverse order.

n = int(input())
while n > 0:
    last_digit = n % 10
    print(last_digit)
    n = n // 10
    