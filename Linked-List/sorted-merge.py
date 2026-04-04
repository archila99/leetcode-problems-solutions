
class ListNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        start = ListNode()
        pointer = start

        while list1 and list2:
            if list1.val < list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            
            pointer = pointer.next

        if list1:
            pointer.next = list1
        else:
            pointer.next = list2

        return start.next

if __name__ == "__main__":
    head1 = ListNode(1)
    head1.next = ListNode(5)
    head1.next.next = ListNode(3)
   

    head2 = ListNode(1)
    head2.next = ListNode(4)
    head2.next.next = ListNode(7)
    
    sol = Solution()
    result = sol.mergeTwoLists(head1, head2)
    
    current = result 

    while current:
        print(current.val, end = " -> ")
        current = current.next

    print(None)

   
            
            
        