# Definition for singly-linked list.
# class ListNode:
# def init(self, val=0, next=None):
# self.val = val
# self.next = next
class Solution: 
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None: 
        if head is None: 
            return head 
        i = head.next 
        prev = head 
        while i: 
            if i.val == prev.val: 
                prev.next = i.next 
            else: 
                prev = prev.next 
                i = i.next 
        return head