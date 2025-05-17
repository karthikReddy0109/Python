# Given an array arr[ ] of size N. Create a linked list from the given array and print the data present in the first node.
class Node:
    def __init__(self, value = 0, next_node = None):
        self.data = value
        self.next = next_node

def array_to_LL(N, arr):
    if N == 0:
        return None
    head = Node(arr[0])
    cur = head
    for num in range(1, N):
        temp = Node(arr[num])
        cur.next = temp
        cur = cur.next
    
    return head

def print_LL(head):
    temp = head
    while temp != None:
        print(temp.data, end = " -> ")
        temp = temp.next

def length_of_LL(head):
    count = 0
    if head == None:
        print("Length is :", count)
    
    temp = head
    while temp != None:
        count += 1
        temp = temp.next
    
    print("Length is :", count)


def main():
    N = int(input("Enter length : "))
    arr = list(map(int, input("Enter array elements : ").split()))
    head = array_to_LL(N, arr)
    print_LL(head)
    length_of_LL(head)
    
main()