# Given a number n, find factorial of natural number n.
# Factorial of a non-negative integer is the multiplication of all positive integers smaller than or equal to n. For example factorial of 6 is 6*5*4*3*2*1 which is 720.
def factorial(i):
    if i == 1:
        return 1
    return i * factorial(i - 1)
def main():
    N = int(input("Enter a number : "))
    res = factorial(N)
    print("Factorial of N is :", res)
main()