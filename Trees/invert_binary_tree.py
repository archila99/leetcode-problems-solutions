from tree_utils import TreeNode, list_to_tree, print_tree

class Solution:
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    root = list_to_tree(nums)
    sol = Solution()
    p_original = print_tree(root)
    print(p_original)

    inverted_root = sol.invertTree(root)
    p_inverted = print_tree(inverted_root)
    print(p_inverted)
    
