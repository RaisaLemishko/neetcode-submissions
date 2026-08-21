# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def reflection(self, head: Optional[ListNode], prev: Optional[ListNode] = None) -> Optional[ListNode]:
        if not head:
            return prev
        else:
            curr = head
            next = curr.next
            curr.next = prev
            return self.reflection(next, curr)