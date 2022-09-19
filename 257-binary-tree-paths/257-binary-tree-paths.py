# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def paths(s, root):
            if not root:
                return 
            if root.left == root.right:
                ans.append(s +  str(root.val))
                return 
            paths(s + str(root.val) + '->', root.left)
            paths(s + str(root.val) + '->', root.right)
        ans = []
        paths('', root)
        return ans
            