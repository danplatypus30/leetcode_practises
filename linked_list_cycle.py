# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare = head
        tortoise = head
        if head == None:
            return False
        hare = hare.next
        if hare != None:
            hare = hare.next # iterate twice
        tortoise = tortoise.next
        while hare != None and hare != tortoise:
            hare = hare.next
            if hare != None:
                hare = hare.next # iterate twice
            tortoise = tortoise.next
        if hare == None:
            return False
        if hare == tortoise:
            return True
        # either one of the above should be true
        print("this should not run")
        return False