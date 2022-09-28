# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        count = 0
        while node:
            count += 1
            node = node.next
        remove = count - n
        if count == 1:
            return 
        if remove == 0:
            return head.next
        
        count = 1
        node = head
        while count < remove:
            node = node.next
            count += 1
            
        node.next = node.next.next
        
        return head
        
            
        