# The merge sort algorithm operates by partitioning an array into smaller subarrays, individually sorting these subarrays, and subsequently combining the sorted subarrays to construct the ultimately sorted array.

# Divide: The unsorted list is divided into two equal-sized sublists until each sublist contains only one element. This is done recursively.

# Conquer: The individual elements are sorted by comparing and merging them. In the merging step, the two sublists are combined to create a new sorted sublist. This process continues until the entire list is sorted.

# Merge: In the merging step, the two sublists are compared, and elements are moved to the new sorted list in the correct order. This process is repeated until all elements from both sublists are included in the sorted list.

# Approach
# If the list has only one element or is empty, it is already sorted.

# Divide the list into two halves.

# Recursively apply MergeSort to both halves.

# Merge the two sorted halves to produce a single sorted list.
def merge(arr, left, mid, right):
    i = left
    j = mid + 1
    n = right - left + 1
    new_arr = []
    while(i <= mid and j <= right):
        if arr[i] <= arr[j]:
            new_arr.append(arr[i])
            i += 1
        else:
            new_arr.append(arr[j])
            j += 1
    
    while i <= mid:
        new_arr.append(arr[i])
        i += 1
    
    while j <= right:
        new_arr.append(arr[j])
        j += 1
    
    for c in range(n):
        arr[left + c] = new_arr[c]
        
def merge_sort(arr, left, right):
    if left == right:
        return 
    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge(arr, left, mid, right)
def main():
    n = int(input("Enter the size of an array : "))
    arr = list(map(int, input("Enter the array elements separated by space : ").split()))
    print("Original Array :", arr)
    merge_sort(arr, 0, n-1)
    print("Modified array : ", arr)
main()
