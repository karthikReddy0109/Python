# Write a program that takes an array 'a' as input and prints the reverse of the array
def reverse_an_array(i, arr, n):
    if i >= n // 2:
        return
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    reverse_an_array(i+1, arr, n)

def main():
    n = int(input("Enter a number : "))
    arr = list(map(int, input().split()))
    reverse_an_array(0, arr, n)
    print(arr)
main()