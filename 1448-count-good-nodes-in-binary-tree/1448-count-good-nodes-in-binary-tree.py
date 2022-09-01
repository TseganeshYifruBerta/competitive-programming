# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count, maxx = [0], [0]
        def dfs(root, m):
            if not root:
                return 
            if root.val >= m:
                m = root.val
                count[0] += 1
            dfs(root.left, m)
            dfs(root.right, m)
        dfs(root, -inf)
        return count[0]