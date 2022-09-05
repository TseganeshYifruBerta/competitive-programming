"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        level = 0
        q = deque([(root, level)])
        ans = [[root.val]]
        while q:
            if level < q[0][1]:
                level = q[0][1]
                temp = []
                for node,l in q:
                    temp.append(node.val)
                ans.append(temp)
            node, l = q.popleft()
            ch = node.children
            for i in ch:
                q.append((i, l + 1))
        return ans