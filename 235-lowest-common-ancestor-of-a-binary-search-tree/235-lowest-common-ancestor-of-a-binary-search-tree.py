# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def dfs(root):
            if not root: return 
            if self.ans: return
            if p.val <= root.val <= q.val or p.val >= root.val >= q.val:
                self.ans = root
                return 
            
            left = dfs(root.left)
            right = dfs(root.right)
        dfs(root)
        return self.ans