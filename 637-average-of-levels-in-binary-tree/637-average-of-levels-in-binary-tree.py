# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level = 0
        ans = [root.val/1]
        q = deque([(root, level)])
        while q:
            if level < q[0][1]:
                level = q[0][1]
                summ = 0
                for node, l in q:
                    summ += node.val
                ans.append(summ / len(q))
            node, lev = q.popleft()
            if node.left:
                q.append((node.left, lev + 1))
            if node.right:
                q.append((node.right, lev + 1))
        return ans
        
        