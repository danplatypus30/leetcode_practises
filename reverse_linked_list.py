# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        if prev == None or prev.next == None:
            return head
        ptr = prev.next
        if ptr.next == None:
            # only 2 items
            ptr.next = prev
            prev.next = None
            return ptr
        follow = ptr.next
        prev.next = None
        while follow != None:
            ptr.next = prev # reverse
            # iterate
            prev = ptr
            ptr = follow
            follow = follow.next
        ptr.next = prev
        return ptr
        