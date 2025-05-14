# You are given an array of positive integers, and your task is to write a C++ program to find the Second Largest Element in the array.
# 6
# 4 5 7 10 10

N = int(input("Enter length of an array : "))
arr = list(map(int, input().split()))
largest = float('-inf')
s_largest = float('-inf')

for num in arr:
    if num > largest:
        s_largest = largest
        largest = num
    
    if num < largest and num > s_largest:
        s_largest = num

print("Second largest", s_largest)