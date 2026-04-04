from tree_utils import TreeNode, list_to_tree

class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        p = root.left
        q = root.right
        return self.isSym(p, q)

    def isSym(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return (self.isSym(p.left, q.right) and self.isSym(p.right, q.left))

if __name__ == "__main__":
    sol = Solution()
    lst = [1,2,2,3,4,4,3]
    root = list_to_tree(lst)

    solution = sol.isSymmetric(root)
    print(solution)