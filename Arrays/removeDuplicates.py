# Given an array of integers, your task is to remove any duplicate elements from the array. After removing duplicates, print the number of unique elements and the modified array.

# Ensure that the first 'k' elements in the array contain the final result, where 'k' is the number of unique elements.

# There are no specific requirements for the order of elements beyond 'k' in the array.

# 6         -> 3
# 3 3 5 5 7 -> 3 5 7 5 7 7
def remove_duplicates(N, arr):
    # my_set = set()
    # for num in arr:
    #     my_set.add(num)
    
    # count = 0
    # for set_el in my_set:
    #     arr[count] = set_el
    #     count += 1
    
    # return count
    i = 0
    for j in range(1, N):
        if arr[j] != arr[i]:
            arr[i+1], arr[j] = arr[j], arr[i+1]
            i += 1
    
    return i+1

def main():
    N = int(input("Enter length : "))
    arr = list(map(int, input("Enter array elements : ").split()))
    unique_count = remove_duplicates(N, arr)
    print("Unique count :", unique_count)
    modified_arr = print(*arr)
main()