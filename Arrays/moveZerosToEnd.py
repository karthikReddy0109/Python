# You are given an array of integers. Your task is to write a program that moves all the zeros in the array to the end while maintaining the order of the non-zero elements.
# 9
# 0 0 3 0 0 5 0 
def move_zeros_to_end(N, arr):
    j = 0
    for i in range(N):
        if arr[i] == 0:
            j = i
            break
    
    for i in range(j+1, N):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr
def main():
    N = int(input("Enter length : "))
    arr = list(map(int, input("Enter array elements : ").split()))
    modified_arr = move_zeros_to_end(N, arr)
    print(*modified_arr)
main()