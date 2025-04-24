# The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones, typically starting with 0 and 1.

# So, it goes like this: 0, 1, 1, 2, 3, 5, 8, 13, and so on, where each number is the sum of the two numbers before it.

def fibonacci(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    return fibonacci(i - 1) + fibonacci(i - 2)
def main():
    N = int(input("Enter a number : "))
    print("Fibonacci of N is :", fibonacci(N))
main()
