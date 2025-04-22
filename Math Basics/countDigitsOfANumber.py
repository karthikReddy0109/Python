# Find the number of digits in a given integer N.
n = int(input())
count = 0
while n > 0:
    count += 1
    n = n // 10

print("No of digits :", count)