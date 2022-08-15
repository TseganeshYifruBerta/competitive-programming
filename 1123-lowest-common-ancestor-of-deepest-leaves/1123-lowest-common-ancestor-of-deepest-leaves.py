# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.ans = None
        @lru_cache(None)
        def findheight(root):
            if not root:
                return 0
            left = findheight(root.left)
            right = findheight(root.right)
            return max(left, right) + 1
        def dfs(root):
            if not root:
                return 
            left = findheight(root.left)
            right = findheight(root.right)
            if left == right:
                self.ans = root
                return 
            if left < right:
                dfs(root.right)
            else:
                dfs(root.left)
        dfs(root)
        return self.ans