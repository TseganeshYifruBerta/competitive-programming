# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        def dfs(root, r, c):
            if not root:
                return 
            d[(c, r)].append(root.val)
            
            left = dfs(root.left, r + 1, c - 1)
            right = dfs(root.right, r + 1, c + 1)
        dfs(root, 0, 0)
        ans = []
        prev = -inf
        for k, v in sorted(d.items()):
            if prev != k[0]:
                ans.append([])
            ans[-1].extend(sorted(v))
            prev = k[0]
        return ans
            