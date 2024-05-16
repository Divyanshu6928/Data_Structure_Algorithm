# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        temp=head
        size=0

        while(temp):
            size+=1
            temp=temp.next
        
        if(size==n):
            newhead=head.next
            return newhead
        
        res=size-n
        temp=head

        while(temp):
            res-=1
            if(res==0):
                break
            temp=temp.next
        
        temp.next=temp.next.next

        return head