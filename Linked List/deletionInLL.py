# Deletion in a Linked List involves removing an element.

# This can be executed by eliminating the element

# At the end (tail)
# At the beginning (head)
# A specific position (kth)
# The node with a specific value (x)

class Node:
    def __init__(self, value, next_node = None):
        self.data = value
        self.next = next_node

def arr_to_LL(N, arr):
    if N == 0:
        return None
    head = Node(arr[0])
    cur = head
    for i in range(1, N):
        temp = Node(arr[i])
        cur.next = temp
        cur = cur.next
    return head

def delete_head(head):
    if head == None:
        return None
    if head.next == None:
        return None
    head = head.next
    return head

def print_LL(head):
    temp = head
    while temp != None:
        print(temp.data, end = " -> ")
        temp = temp.next
    print()

def delete_tail(head):
    if head == None:
        return None
    if head.next == None:
        return None
    
    temp = head
    while temp.next.next != None:
        temp = temp.next
    
    temp.next = None
    return head

def delete_Kth_node(head, k):
    if k == 0:
        head = delete_head(head)
    count = 0
    temp = head
    while temp.next != None:
        count += 1
        if count == k - 1:
            break
        temp = temp.next
    
    if temp.next == None:
        delete_tail(head)
    temp.next = temp.next.next
    return head

def main():
    N = int(input("Enter length : "))
    k = int(input("Enter a value for K : "))
    arr = list(map(int, input("Enter array elements : ").split()))
    head = arr_to_LL(N, arr)
    print_LL(head)
    # head = delete_head(head)
    # print("After deleting head : ")
    # print_LL(head)
    # head = delete_tail(head)
    # print("After deleting tail : ")
    # print_LL(head)
    head = delete_Kth_node(head, k)
    print("After deleting kth pos :")
    print_LL(head)
main()