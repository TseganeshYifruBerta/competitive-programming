# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(arr):
            if len(arr) == 0:
                return 
            maxx = max(arr)
            idx = arr.index(maxx)
            new_node = TreeNode(maxx)
            new_node.left = helper(arr[:idx])
            new_node.right = helper(arr[idx + 1:])
            return new_node
        
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        inOrder = inorder(root)
        inOrder.append(val)
        return helper(inOrder)