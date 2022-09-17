# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
#         check wether the leaf is equal to the target if so we have to delete it(return True)
        def check(root):
            if root.left == root.right and root.val == target:
                return True
            
            
        def dfs(root):
		
# if root.val equals to target and root is leaf node return False
            if check(root): return False
            
			
# if root.val is not equal to target and root is leaf node return True
            if root.left == root.right:
                return True
            
# if root.left is leaf and it's val is equal to target root.left = None(delete the node)
            if root.left and not dfs(root.left):
                root.left = None
            
# if root.right is leaf and it's val is equal to target root.left = None(delete the node)
            if root.right and not dfs(root.right):
                root.right = None
                
# if we delete both right and left then we have to check root.val, if it is equal to target the we have to delete that node too
            if check(root): return False
			
            return True
        
# calling the function
        dfs(root)
		
# after doing all we have to check if the root (if it is leaf and its val == target) then we have to delete it too
        if check(root): return
        return root