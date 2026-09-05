# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev= None
        cur = head#存的是1的引用
        #想象一个链表1->2->3要改成1<-2<-3
        #注意他们的位置是不变的就是动了箭头
        #不是1->2->3变成3->2->1
        while cur:
            #先存着后面要用现在存的是2的引用
            nxt= cur.next
            #把2的引用指向了None
            cur.next=prev
            #把None引用指向了1的引用这样传递完就是2-None-1
            prev = cur
            #此时cur仍然是head：1那应该让cur指向1啊我草你妈的为什么要换成2马上不就要进新的节点了吗
            #哦原来是你要注意啊位置是不变的只是动箭头，这个时候就要互换2和3之间的箭头了
            cur = nxt
        return prev  
            
            