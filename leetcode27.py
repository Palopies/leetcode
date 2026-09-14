# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        first = list1
        second = list2
        
        while first is not None and second is not None:
            if first.val >=second.val:
                tail.next = second
                second=second.next
            else:
                tail.next = first
                first = first.next
            tail = tail.next
        
        if first is not None:
            tail.next = first
        else:
            tail.next = second
        return dummy.next