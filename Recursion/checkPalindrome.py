# Develop a program that receives an input string 's' and verifies whether it is a palindrome or not
def check_palindrome(i, s, n):
    if i >= n // 2:
        return True
    if s[i] != s[n - i - 1]:
        return False
    return check_palindrome(i+1, s, n)
def main():
    n = int(input("Enter length of string : "))
    s = input()
    print(check_palindrome(0, s, n))
main()