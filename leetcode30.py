# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        
        dummy = ListNode(0)
        dummy.next = head
        pre =dummy
        while pre.next and pre.next.next :
            a = pre.next
            b = pre.next.next
            a.next = b.next
            b.next =  a
            pre.next = b
            
            pre =a 
        return dummy.next
