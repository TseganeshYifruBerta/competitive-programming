# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(root, summ):
            if not root:
                return False
            if root.left == root.right:
                if root.val + summ < limit:
                    return False
                return True
            left, right = False, False
            if root.left:
                left = dfs(root.left, summ + root.val)
            if root.right:
                right = dfs(root.right, summ + root.val)
            if not left:
                root.left = None
            if not right:
                root.right = None
            return left or right
        dfs(root, 0)
        if root.left == root.right and root.val < limit:
            return
        return root
            
                
        