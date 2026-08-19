# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        current_node = head
        gaps = []
        # collect all pointers in memory linear array
        while current_node:
            gaps.append(current_node)
            current_node = current_node.next

        length_list = len(gaps)
        # array will be cuttoff here
        gaps[length_list // 2].next = None

        # now iterate through half of the array that has
        # to be "filled" with the later half 
        # get the smaller half when splitting
        for i in range(math.ceil(length_list / 2) - 1):
            # node at the end that will fill the gap
            to_move = gaps[length_list - (i + 1)] # expands to -i - 1
            to_move.next = gaps[i].next
            gaps[i].next = to_move


        


        