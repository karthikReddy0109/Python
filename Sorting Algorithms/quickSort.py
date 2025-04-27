# QuickSort is a sorting algorithm that selects an element as a pivot and reorganizes the array by positioning the pivot in its appropriate place within the sorted array.

def partition(arr, low, high):
    i = low
    j = high
    while i < j:
        while arr[i] <= arr[low] and i <= high - 1:
            i += 1
        while arr[j] > arr[low] and j >= 1:
            j -= 1
        if i < j:
            # Swap arr[i] and arr[j]
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    # Swap arr[low] and arr[j]
    temp = arr[low]
    arr[low] = arr[j]
    arr[j] = temp
    return j

def quick_sort(arr, low, high):
    if low < high:
        j = partition(arr, low, high)
        quick_sort(arr, low, j-1)
        quick_sort(arr, j+1, high)

# Input: 5 \n 64 25 12 22 11
n = int(input())
arr = list(map(int, input().split()))
quick_sort(arr, 0, n-1)
print(*arr)