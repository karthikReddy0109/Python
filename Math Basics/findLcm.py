a = int(input())
b = int(input())
if a > b:
    greater = a
else:
    greater = b

count = 1
while True:
    multiple = greater * count
    if (multiple % a == 0) and (multiple % b == 0):
        print("LCM IS :", multiple)
        break
    count += 1