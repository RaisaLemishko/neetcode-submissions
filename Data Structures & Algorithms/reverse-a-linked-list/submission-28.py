# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reflection(head)

    def reflection(self, head: Optional[ListNode], prev: Optional[ListNode] = None) -> Optional[ListNode]:
        
        if not head:
            return prev
        else:
            curr = head
            next_node = curr.next
            curr.next = prev
            return self.reflection(next_node, curr)