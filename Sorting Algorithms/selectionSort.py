# Selection sort is a basic way to sort a list. It finds the smallest item and puts it at the front until the whole list is sorted in ascending order.
# 30 50 40 20 -----> 10 20 30 40 
def selection_sort(N, arr):
    for i in range(N-1):
        min_index = i
        for j in range(i+1, N):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]

def main():
    N = int(input())
    arr = list(map(int, input().split()))
    selection_sort(N, arr)
    print(arr)
main()