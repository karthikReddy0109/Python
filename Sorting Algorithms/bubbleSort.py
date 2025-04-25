# Bubble sort is a basic sorting method for a list of items, where it repeatedly compares and swaps adjacent items to move the larger ones to the end of the list until the entire list is sorted
#     30 50 40 20 10 -----> 10 20 30 40 50
def bubble_sort(n, arr):
    total_loop_count = 0
    is_swapped = False
    for i in range(n-1, 0, -1):
        count = 0
        for j in range(0, i):
            count += 1
            if arr[j] > arr[j+1]:
                is_swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        total_loop_count += count
        if not(is_swapped):
            break
    print("Total loop count =", total_loop_count)
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    bubble_sort(n, arr)
    print(arr)
main()