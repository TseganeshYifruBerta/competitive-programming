# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def helper(root, freq):
#     everytime increment the frequency of that number by one
            freq[root.val] += 1
    
    
#     if it is leaf we have to check whether one of its permutation can form a palindromic path or not
#     easily we can check if their is more than one odd frequency it means this path cannot for a palindrom if not we can count as one valid path
            if root.left == root.right:
                c = 0
                for i in freq:
                    if freq[i] % 2 : c += 1
                    if c > 1: return 
                    
                self.count += 1
                return 
#     if it has left node or right node we call it recursively 
            if root.left : helper(root.left, freq.copy())
            if root.right: helper(root.right, freq.copy())
            
#     finaly we can call our helper function and return our count
        helper(root, defaultdict(int))
        return self.count