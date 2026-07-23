# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# can I modify the input?
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        tail = head
        while tail not in seen: # O(n)
            if not tail:
                return False
            seen.add(tail)
            tail = tail.next # O(n)

            # So O(n*n) -> not good

        return True

        