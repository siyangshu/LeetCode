# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        hasCommonAncestor, result = self.isIn(root, p, q)
        return result
    
    def isIn(self, tree, p, q):
        if tree == None:
            return False, None
        if tree == q or tree == p:
            hasCommonAncestor, result = self.isIn(tree.left, p, q)
            if result != None:
                return True, tree
            else:
                hasCommonAncestor, result = self.isIn(tree.right, p, q)
                if result != None:
                    return True, tree
                else:
                    return False, tree
        else:
            hasCommonAncestor, result = self.isIn(tree.left, p, q)
            if hasCommonAncestor:
                return True, result
            elif result != None:
                hasCommonAncestor, result = self.isIn(tree.right, p, q)
                if result != None:
                    return True, tree
                else:
                    return False, tree
            else:
                return self.isIn(tree.right, p, q)
            
        
