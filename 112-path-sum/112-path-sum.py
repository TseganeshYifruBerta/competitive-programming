# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def pathSum(root, summ):
            if not root: return False
            if root.left == root.right:
                if summ + root.val == targetSum: return True
                return False
            
            return pathSum(root.left, summ + root.val) or pathSum(root.right, summ + root.val)
        
        return pathSum(root, 0)
                