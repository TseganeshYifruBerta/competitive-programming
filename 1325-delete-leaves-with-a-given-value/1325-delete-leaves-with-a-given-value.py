# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        
        def helper(root):
            if root.left == root.right:
                if root.val == target:
                    return False
                return True
            
            
            if root.left and not helper(root.left):
                root.left = None
            if root.right and not helper(root.right):
                root.right = None
                
                
            if root.left == root.right and root.val == target:
                return False
            return True
        
        
        helper(root)
        if root.left == root.right and root.val == target:
            return 
        return root