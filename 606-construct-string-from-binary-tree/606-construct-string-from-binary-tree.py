class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        string = str(root.val)
        if root.left: 
            string += "(" + self.tree2str(root.left) + ")"
        if root.right:
            if not root.left: string += "()"
            string += "(" + self.tree2str(root.right) + ")"
        return string