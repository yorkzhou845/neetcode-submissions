# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        flag = 0
        prev = head or None
        while head:
            next = head.next or None
            head.next = prev
            if flag == 0: 
                prev.next = None
                flag = 1
            prev = head
            head = next        
        return prev#head is always None when the while loop ends so return prev
        

        