# 938. Range Sum of BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = 0
    def rangeSumBST(self, root, L, R):
        def dfs(root):
            if root:
                if L <= root.val <= R: self.ans += root.val
                if L <= root.val: dfs(root.left)
                if R >= root.val: dfs(root.right)
        
        self.ans = 0
        dfs(root)
        return self.ans

    def rangeSumBST2(self, root, L, R):
        if not root: return 0
        ans, left, right = 0, 0, 0
        if L <= root.val <= R: ans += root.val
        if L <= root.val: left = self.rangeSumBST(root.left, L, R)
        if R >= root.val: right = self.rangeSumBST(root.right, L, R)
        return ans + left + right

    def rangeSumBST3(self, root, L, R):
        if not root: return 0
        return (0, root.val)[L <= root.val <= R] + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)

    # iterative
    def rangeSumBST4(self, root, L, R):
        stack, ans = [root], 0
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R: ans += node.val
                if L <= node.val: stack.append(node.left)
                if R >= node.val: stack.append(node.right)
        return ans