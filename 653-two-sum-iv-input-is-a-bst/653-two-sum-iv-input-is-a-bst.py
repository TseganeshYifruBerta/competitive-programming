# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        
        inorder = inorder(root)
        p1, p2 = 0, len(inorder) - 1
        
        while p2 > p1:
            if inorder[p2] + inorder[p1] == k: return True
            if inorder[p2] + inorder[p1] > k: p2 -= 1
            else: p1 += 1
                
                
        return False
            