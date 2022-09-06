# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root):
            if not root:
                return False, None
            if root.left == root.right:
                if root.val == 1:
                    return True, TreeNode(root.val)
                return False, None
            newNode = TreeNode(root.val)
            left = helper(root.left)
            right = helper(root.right)
            if not left[0] and not right[0] and root.val == 0:
                return False, None
            if left[0]:
                newNode.left = left[1]
            if right[0]:
                newNode.right = right[1]
            return True, newNode
        return helper(root)[1]