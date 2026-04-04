from tree_utils import TreeNode, list_to_tree

class Solution:
    def rangeSumBST(self, root, low, high):
        if not root:
            return 0
        
        if root.val < low:
            # skip left subtree
            return self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            # skip right subtree
            return self.rangeSumBST(root.left, low, high)
        else:
            return (root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high))


if __name__ == "__main__":
    sol = Solution()
    lst = [10,5,15,3,7,None,18]
    root = list_to_tree(lst)
    low = 7
    high = 15
    solution = sol.rangeSumBST(root, low, high)
    print(solution)