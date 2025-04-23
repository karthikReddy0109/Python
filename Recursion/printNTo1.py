def print_N_to_1(i):
    if i == 0:
        return 
    print(i)
    print_N_to_1(i-1)

def main():
    N = int(input("Enter a Number : "))
    print_N_to_1(N)
main()