# Determine whether a given number N is a prime number, where a prime number is defined as a number that is divisible only by 1 and itself.
# For the input integer 7, the program calculates the count of its divisors. Since 7 has only two divisors (1 and 7), the count is 2, indicating that it's a prime number.
N = int(input())
is_prime = True
for i in range(2, N):
    if N % i == 0:
        is_prime = False

print(is_prime)
