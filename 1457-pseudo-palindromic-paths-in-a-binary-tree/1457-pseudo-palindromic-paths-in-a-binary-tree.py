# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def helper(root, d):
            if root.left == root.right:
                d[root.val] += 1
                c = 0
                for i in d:
                    if d[i] % 2 :
                        c += 1
                    if c > 1:
                        return 
                self.count += 1
                return 
            
            d[root.val] += 1
            if root.left :
                helper(root.left, d.copy())
            if root.right:
                helper(root.right, d.copy())
        helper(root, defaultdict(int))
        return self.count