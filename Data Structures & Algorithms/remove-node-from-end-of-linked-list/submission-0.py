# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head is None:
            return None

        slow = head
        fast = head
        prev = None
        for _ in range(n):
            fast = fast.next

        while slow and fast:
            prev = slow
            slow = slow.next
            fast = fast.next



        current = slow
        # remove item (skip the gap)
        # if item is in the end it should also be already handled (sets prev.next to None)
        if prev:
            prev.next = current.next
        else:
            # in case first item is the one to be removed
            head = current.next

        return head
