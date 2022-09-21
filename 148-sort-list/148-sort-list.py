# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst=[]
        node, node1 = head, head
        while node:
            lst.append(node.val)
            node = node.next
        lst.sort()
        p = 0
        while node1:
            node1.val = lst[p]
            node1 = node1.next
            p += 1
        return head
        