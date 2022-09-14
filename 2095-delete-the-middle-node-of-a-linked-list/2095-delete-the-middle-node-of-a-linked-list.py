# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        node, n = head, head
        while n:
            count += 1
            n = n.next
        mid = count // 2
        count = 0
        while node:
            count += 1
            if count == mid:
                node.next = node.next.next
                return head
            node = node.next
            