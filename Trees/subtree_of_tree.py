from tree_utils import TreeNode, list_to_tree
from same_btree import Solution

class Sol:
    def __init__(self):
        self.helper = Solution()

    def isSubtree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        
        if root.val == subRoot.val:
            if self.helper.isSameTree(root, subRoot):
                return True
        
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot)) 

if __name__ == '__main__':
    root_list = [3,4,5,1,None,2]
    subRoot_list = [3,1,2]

    root = list_to_tree(root_list)
    subRoot = list_to_tree(subRoot_list)

    sol = Sol()
    result = sol.isSubtree(root, subRoot)

    print(result)
        