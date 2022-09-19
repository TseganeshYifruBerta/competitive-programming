# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def buildTree(arr):
            if not arr:
                return 
            minn = inf
            for i in range(len(arr)):
                if d[minn] > d[arr[i]]:
                    minn = arr[i]
                    
            idx = arr.index(minn)
            new_node = TreeNode(minn)
            new_node.left = buildTree(arr[:idx])
            new_node.right = buildTree(arr[idx + 1:])
            return new_node
            
        d = {}
        postorder.reverse()
        d[inf] = inf
        for i in range(len(postorder)):
            d[postorder[i]] = i
            
        return buildTree(inorder)
            
        
            