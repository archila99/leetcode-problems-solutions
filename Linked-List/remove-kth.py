class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def delete_k(head, k):

    if head is None or k <= 0:
        return head

    curr = head 
    prev = None

    count = 0

    while curr is not None:
        count += 1

        if count % k == 0:
            if prev is not None:
                prev.next = curr.next
            else:
                head = curr.next
        
        else: 
            prev = curr
        
        curr = curr.next

    return head

def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end = " ")
        curr = curr.next
    
    print()

if __name__ == "__main__":
    # Create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6
    head = Node(1)
    head.next = Node(5)
    head.next.next = Node(3)
    head.next.next.next = Node(23)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    k = 2
    head = delete_k(head, k)
    print_list(head)