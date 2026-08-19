# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n) space
# O(n) time
# can be improved to:
# O(2n) time
# O(1) space
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return
        slow = head
        fast = head
        gaps = []
        # collect all pointers in memory linear array
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # reverse second half
        current = slow.next
        next_node = None
        # starting with this condition makes middle point be the end of the array
        prev = None
        while current:
            next_node = current.next

            current.next = prev

            prev = current


            current = next_node

        slow.next = None
        
        # interleave arrays
        # it is find to just iterate until the end because we already marked the 
        # middle point .next as None so it actually ends
        first_half = head
        # prev here would be the first element of the reversed array
        second_half = prev
        while first_half and second_half:
            # temp vars
            n_f_h = first_half.next
            n_s_h = second_half.next
            # iterleave
            first_half.next = second_half
            second_half.next = n_f_h
            # for the next iteration
            first_half = n_f_h
            second_half = n_s_h

            




        


        