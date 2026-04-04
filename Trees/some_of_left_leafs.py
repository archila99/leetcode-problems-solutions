from tree_utils import TreeNode, list_to_tree

class Solution:
    def sumLeftLeaf(self, root):
        if not root:
            return 0
        
        res = 0
        if root.left and not root.left.left and not root.left.right:
            res += root.left.val
        
        res += self.sumLeftLeaf(root.left)
        res += self.sumLeftLeaf(root.right)

        return res

if __name__ == "__main__":
    lst = [3,9,20,None,None,15,7]
    root = list_to_tree(lst)

    sol = Solution()
    print(sol.sumLeftLeaf(root))