# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# can I modify the input?
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = []
        tail = head
        while tail not in seen:
            if not tail:
                return False
            seen.append(tail)
            tail = tail.next

        return True

        