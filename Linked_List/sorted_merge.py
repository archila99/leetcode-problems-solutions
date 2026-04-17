
class ListNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Merged(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        new_head = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                new_head.next = list1
                list1 = list1.next
            else:
                new_head.next = list2
                list2 = list2.next
            new_head = new_head.next
        
        new_head.next = list1 if list1 else list2

        return dummy.next

if __name__ == "__main__":
    head1 = ListNode(1)
    head1.next = ListNode(5)
    head1.next.next = ListNode(3)
   

    head2 = ListNode(1)
    head2.next = ListNode(4)
    head2.next.next = ListNode(7)
    
    sol = Merged()
    result = sol.mergeTwoLists(head1, head2)
    
    current = result 

    while current:
        print(current.val, end = " -> ")
        current = current.next

    print(None)

   
            
            
        