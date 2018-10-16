# 235. Lowest Common Ancestor of a Binary Search Tree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        left = self.lowestCommonAncestor(root, p, q)
        right = self.lowestCommonAncestor(root, p, q)
        if left and right:
            return root
        node = None
        if (root.val == p.val or root.val == q.val):
            node = root
        if (node and left) or (node and right):
            return root
        if left:
            return left
        if right:
            return right
        return node

    def lowestCommonAncestor2(self, root, p, q):
        if not root:
            return None
        
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root



        

        