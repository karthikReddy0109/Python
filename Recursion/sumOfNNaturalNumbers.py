# Given a number n, find sum of first n natural numbers.
def sum_of_n_numbers(i, is_sum, N):
    if i == N+1:
        return is_sum
    return sum_of_n_numbers(i+1, is_sum + i, N)
def main():
    N = int(input("Enter a number : "))
    result = sum_of_n_numbers(1, 0, N)
    print("Sum of N Natural number is :", result)
main()