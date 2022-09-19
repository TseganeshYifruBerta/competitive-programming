# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def build(arr):
            if not arr:
                return 
            mid = len(arr) // 2
            new_node = TreeNode(arr[mid])
            new_node.left = build(arr[:mid])
            new_node.right = build(arr[mid + 1:])
            return new_node
        inorder = []
        while head:
            inorder.append(head.val)
            head = head.next
        return build(inorder)
        