# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def pathSum(root, lst):
            
            if root.left == root.right:
                if sum(lst) + root.val == targetSum:
                    ans.append(lst + [root.val])
                return 
            
            if root.left:
                pathSum(root.left, lst + [root.val])
            if root.right:
                pathSum(root.right, lst + [root.val])
                
        if not root:
            return
        
        ans = []
        pathSum(root, [])
        return ans