# You are given an array of positive integers, and your task is to find the largest element in the array.

N = int(input())
arr = list(map(int, input().split()))
largest = float('-inf')
for num in arr:
    if num > largest:
        largest = num

print("Largest number is", largest)
