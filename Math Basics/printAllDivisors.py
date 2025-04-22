# Print all the divisors of the integer N in ascending order, given the integer N.
# For the input integer 12, the program calculates and prints all its divisors in ascending order. The divisors of 12 are 1, 2, 3, 4, 6, 12.

N = int(input())
for i in range(1, N+1):
    if (N % i == 0):
        print(i)