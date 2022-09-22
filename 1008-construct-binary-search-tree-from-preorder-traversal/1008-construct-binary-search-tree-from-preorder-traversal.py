# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(pre_lst, in_lst):
            if not in_lst or not pre_lst:
                return None
            root = TreeNode(pre_lst[0])
            mid = in_lst.index(pre_lst[0])
            root.left = helper(pre_lst[1:mid + 1], in_lst[:mid])
            root.right = helper(pre_lst[mid + 1:], in_lst[mid + 1:])
            return root
        inorder = sorted(preorder)
        return helper(preorder, inorder)