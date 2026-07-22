# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        previous_item: Optional[ListNode] = None
        current_item: Optional[ListNode] = head

        while current_item:
            next_item = current_item.next

            # head becomes tail
            current_item.next = previous_item

            previous_item = current_item

            current_item = next_item

        return previous_item
