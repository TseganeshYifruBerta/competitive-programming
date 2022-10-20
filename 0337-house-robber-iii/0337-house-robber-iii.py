# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(node):
            if not node:
                return 0,0
            if not node.right and not node.left:
                return node.val, 0
            
            left, left_child = dfs(node.left)
            right, right_child = dfs(node.right)
            
            child_sum = left_child + right_child
            my_sum = left + right
            sib_left = left + right_child
            sib_right = right + left_child
            max_ = max(my_sum, child_sum, sib_left, sib_right)
            
            return child_sum + node.val, max_
        
        left,right = dfs(root)
        answer = max(left,right)
        return answer
        