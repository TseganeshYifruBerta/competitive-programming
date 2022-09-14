# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        lst = []
        node = head
        while head:
            lst.append(head.val)
            head = head.next
        ans = []
        l, r = 0 , len(lst) - 1
        while r > l:
            ans.append(lst[l])
            ans.append(lst[r])
            l += 1
            r -= 1
        if len(lst) % 2:
            ans.append(lst[l])
        for i in ans:
            node.val = i
            node = node.next