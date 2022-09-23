# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.maxx = 1
        def dfs(root, val):
            if root.right == root.left:
                if root.val == val:
                    return 1
                return 0
            
            left, right = 0, 0
            if root.left:
                left = dfs(root.left, root.val)
                
            if root.right:
                right = dfs(root.right, root.val)
                
            self.maxx = max(self.maxx, left + right + 1)
            if root.val == val:
                return max(right , left) + 1
            
            return 0
        if not root:
            return 0
        dfs(root, root.val)
        return self.maxx - 1
        
                