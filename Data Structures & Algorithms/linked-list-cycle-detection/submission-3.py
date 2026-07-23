# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# can I modify the input?
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and slow:

            if fast.next:
                fast = fast.next.next
            else:
                return False

            
            if slow == fast:
                return True
    
    
            slow = slow.next 

            
            

            # So O(n*n) -> not good

        return False

        