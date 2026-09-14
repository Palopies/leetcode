# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first= l1
        second = l2
        dummy = ListNode()
        tail =dummy
        carry=0
        while first!=None or second!=None or carry != 0:
            x = first.val if first is not None else 0
            y= second.val if second is not None else 0 
            total = x+ y + carry
            digit = total%10
            carry = total // 10
            tail.next = ListNode(digit)
            tail = tail.next
            if first is not None:
                first=first.next
            if second is not None:
                second = second.next
        return dummy.next
            
            