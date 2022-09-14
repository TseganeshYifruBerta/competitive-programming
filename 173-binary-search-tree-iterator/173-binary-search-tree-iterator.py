# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        def helper(root):
            if not root:
                return []
            return helper(root.left) + [root.val] + helper(root.right)
        self.inorder = helper(root)
        self.count = 0

    def next(self) -> int:
        ans = self.inorder[self.count]
        self.count += 1
        return ans
        

    def hasNext(self) -> bool:
        return self.count < len(self.inorder)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()