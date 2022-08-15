# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.ans = None
        def dfs(root):
            if not root:
                return 
            if root.val > val:
                dfs(root.left)
            elif root.val < val:
                dfs(root.right)
            else:
                self.ans = root
        dfs(root)
        return self.ans