# Insertion sort is a simple sorting method that divides a list into two parts: a part that's already sorted and an unsorted part.

# It then repeatedly selects an item from the unsorted part and places it in its appropriate position within the sorted part

# This continues until the entire list is in the correct order
def insertion_sort(n, arr):
    for i in range(1, n):
        j = i
        while(arr[j] < arr[j-1] and j >= 1):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    insertion_sort(n, arr)
    print(arr)
main()