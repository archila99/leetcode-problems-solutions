from sorted_merge import ListNode, Merged

class Solution:
    def mergedKLists(self, lists):
        if not lists:
            return None
        
        m = Merged()

        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(m.mergeTwoLists(l1, l2))

            lists = merged

        return lists[0]


def main():
    def build_linked_list(arr):
        dummy = ListNode(0)
        cur = dummy

        for num in arr:
            cur.next = ListNode(num)
            cur = cur.next

        return dummy.next
    
    lists = [[1,4,5],[1,3,4],[2,6]]
    linked_lists = [build_linked_list(lst) for lst in lists]

    sol = Solution()
    result = sol.mergedKLists(linked_lists)

    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")

if __name__ == "__main__":
    main()