# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def helper(root):
            if not root:
                return '()'
            res = str(root.val)
            left = helper(root.left)
            right = helper(root.right)
            if left == '()' and right == '()':
                return '(' + str(root.val) + ')'
            if left == '()' and right != '()':
                res += left + right
            elif left != '()' and right != '()':
                res += left + right
            else:
                res += left
            return  '(' + res + ')'
        ans = helper(root)
        ans = ans[1:len(ans) - 1]
        return ans
                