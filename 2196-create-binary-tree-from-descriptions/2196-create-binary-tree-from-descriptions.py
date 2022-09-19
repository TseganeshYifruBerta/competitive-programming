# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        seen = {}
        def build(root):
            if not root:
                return 
            if root in seen:
                return seen[root]
            new_node = TreeNode(root)
            for i in d[root]:
                if i[1] == 1:
                    new_node.left = build(i[0])
                else:
                    new_node.right = build(i[0])
            seen[root] = new_node
            return new_node
        
        d = defaultdict(list)
        for i in descriptions:
            d[i[0]].append((i[1], i[2]))
        childs = set()
        for i in descriptions:
            childs.add(i[1])
            
        ans = None
        for i in descriptions:
            if i[0] not in childs:
                ans = i[0]
        return build(ans)