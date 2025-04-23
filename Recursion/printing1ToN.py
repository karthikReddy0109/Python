def print_1_to_N(i, N):
    if i == N+1:
        return 
    print(i)
    print_1_to_N(i+1, N)
    
def main():
    N = int(input("Enter a number : "))
    print_1_to_N(1, N)
main()