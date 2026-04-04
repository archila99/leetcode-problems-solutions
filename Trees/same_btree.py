from tree_utils import list_to_tree, TreeNode

class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))
    

if __name__ == '__main__':
    p_list = [1,2,3]
    q_list = [1,2,3]
    p = list_to_tree(p_list)
    q = list_to_tree(q_list)

    sol = Solution()
    result = sol.isSameTree(p, q)
    print(result)