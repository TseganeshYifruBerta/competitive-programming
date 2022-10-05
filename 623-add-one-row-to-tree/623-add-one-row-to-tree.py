# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        level = 1
        q = deque([(root, level)])
        
        if depth - 1 == 0:
            new = TreeNode(val)
            new.left = root
            return new
        
        
        while q:
            if level < q[0][1]:
                level = q[0][1]
            
            
            if level == depth - 1:
                for i in range(len(q)):
                    left, right = q[i][0].left, q[i][0].right
                    q[i][0].left = TreeNode(val)
                    q[i][0].right = TreeNode(val)
                    q[i][0].left.left, q[i][0].right.right = left, right
                break
                
            node, dep = q.popleft()
            if node.left:
                q.append((node.left, dep + 1))
            if node.right:
                q.append((node.right, dep + 1))
        
        return root