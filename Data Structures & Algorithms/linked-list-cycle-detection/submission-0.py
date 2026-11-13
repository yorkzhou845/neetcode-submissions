# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        try: fast = head.next.next
        except AttributeError: return False

        while fast:
            if slow == fast: return True
            slow = slow.next
            try: fast = fast.next.next
            except AttributeError: return False
        return False

        