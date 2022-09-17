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
            minn, maxx = inf, -inf
            if root.left:
                left = helper(root.left)
                self.maxx = max(self.maxx, abs(root.val - left[0]), abs(root.val - left[1]))
                minn = left[0]
                maxx = left[1]
            if root.right:
                right = helper(root.right)
                self.maxx = max(self.maxx, abs(root.val - right[0]), abs(root.val - right[1]))
                minn = min(minn, right[0])
                maxx = max(maxx, right[1])
            return [min(minn, root.val), max(maxx, root.val)]
        helper(root)
        return self.maxx