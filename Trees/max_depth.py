from tree_utils import TreeNode, list_to_tree

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)

if __name__ == "__main__":
    lst = [1,2,3,None,None,4]
    root = list_to_tree(lst)

    sol = Solution()
    print(sol.maxDepth(root))
