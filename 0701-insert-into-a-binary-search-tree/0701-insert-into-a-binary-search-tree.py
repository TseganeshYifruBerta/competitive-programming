# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.node = TreeNode(val)
        def dfs(root):
            if not root: return
            if root.right == root.left:
                if root.val < val:
                    root.right = self.node 
                else:
                    root.left = self.node 
                return
            if root.val < val:
                if root.right:
                    dfs(root.right)
                else:
                    root.right = self.node 
                    return 
            elif root.val > val:
                if root.left:
                    dfs(root.left)
                else:
                    root.left = self.node 
                    return
        dfs(root)
        if not root:
            return self.node 
        return root
                    