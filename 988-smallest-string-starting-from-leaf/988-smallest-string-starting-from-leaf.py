# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def paths(s, root):
            if not root:
                return 
            if root.left == root.right:
                a = s +  chr(root.val + 97)
                ans.append(a[::-1])
                return 
            paths(s + chr(root.val + 97), root.left)
            paths(s + chr(root.val + 97), root.right)
        ans = []
        paths('', root)
        ans.sort()
        return ans[0]