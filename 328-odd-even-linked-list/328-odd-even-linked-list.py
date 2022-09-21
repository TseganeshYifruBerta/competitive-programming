# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = []
        even = []
        node, p = head, 1
        while node:
            if p % 2:
                odd.append(node.val)
            else:
                even.append(node.val)
            node = node.next
            p += 1
        lst = odd + even
        p, node1 = 0, head
        while node1:
            node1.val = lst[p]
            node1 = node1.next
            p += 1
        return head
            