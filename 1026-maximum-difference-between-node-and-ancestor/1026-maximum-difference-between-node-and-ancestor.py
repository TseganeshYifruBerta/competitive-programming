# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.maxx = 0
        def helper(root):
            if root.left == root.right:
                return [root.val, root.val]
            
            minn, maxx, val = inf, -inf, root.val
            
            if root.left:
                lMin, lMax = helper(root.left)
                self.maxx = max(self.maxx, abs(val - lMin), abs(val - lMax))
                minn, maxx = lMin, lMax
                
            if root.right:
                rMin, rMax = helper(root.right)
                self.maxx = max(self.maxx, abs(val - rMin), abs(val - rMax))
                minn, maxx = min(minn, rMin),  max(maxx, rMax)
                
            return [min(minn, val), max(maxx, val)]
        helper(root)
        return self.maxx