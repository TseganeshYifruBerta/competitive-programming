# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def helper(root):
            if not root:
                return False
            if root.left == root.right:
                if root.val == target:
                    return False
                return True
            left = helper(root.left)
            right = helper(root.right)
            
            if not left:
                root.left = None
            if not right:
                root.right = None
            if not right and not left and root.val == target:
                return False
            return True
        
        helper(root)
        if root.left == root.right and root.val == target:
            return 
        return root