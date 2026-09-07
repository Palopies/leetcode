# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         arr = []
#         cur = head
#         while cur:
#             arr.append(cur.val)
#             cur = cur.next
#         left = 0
#         right = len(arr)-1
#         while left<right:
#             if arr[left]!=arr[right]:
#                 return False
#             right-=1
#             left+=1
#         return True
class Solution:
     def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
             return True
        slow = head
        fast = head
        while fast.next and fast.next.next:
             slow = slow.next
             fast = fast.next.next
        def reverse(node):
            prev = None 
            cur = node
            while cur:
                nxt= cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        second_head = reverse(slow.next)
        p1 = head 
        p2 = second_head
        Flag= True
        while Flag and p2:
            if p1.val!=p2.val:
                Flag = False
            p1=p1.next
            p2= p2.next
        slow.next = reverse(second_head)
        return Flag