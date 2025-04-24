def print_N_to_1(i, N):
    if i == N+1:
        return 
    print_N_to_1(i+1, N)
    print(i)
    

def main():
    N = int(input("Enter a Number : "))
    print_N_to_1(1, N)
main()