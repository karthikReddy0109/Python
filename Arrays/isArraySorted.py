# Write a program that takes an integer array a of length n and prints 1 if the array is sorted in ascending order; otherwise, it prints 0.
def check_if_arr_sorted(n, a):
    if n == 1:
        return True
    for i in range(1, n):
        if a[i] >= a[i-1]:
            pass
        else:
            return False
    return True
def main():
    n = int(input("Enter length : "))
    a = list(map(int, input("Enter array elements : ").split()))
    result = check_if_arr_sorted(n, a)
    print("Result :", result)
main()