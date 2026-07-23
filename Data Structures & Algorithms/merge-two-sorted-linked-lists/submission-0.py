# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # two pointer problem i guess
        # go over the arrays until one is bigger then the other

        # get rid of initial condition where both of them are None
        
        if list1 and list2:
            def choose_next_pointer(a: ListNode ,b: ListNode , tail:  Optional[ListNode]): # returns the new tail aswell

                if a.val <= b.val:
                    if tail:
                        tail.next = a
                    tail = a

                    if a.next:
                        choose_next_pointer(a.next, b, tail)
                    else:
                        # A has finished and it is smaller than or equal to B
                        # but the next A is None 
                        tail.next = b
                        return None
                else:
                    if tail:
                        tail.next = b
                    tail = b

                    if b.next:
                        tail.next

                        choose_next_pointer(a, b.next, tail)
                    else:
                        # B has finished and it is smaller than A
                        # but the next A is None 
                        tail.next = a
                        return None

            a = list1
            b = list2
            if a.val <= b.val:
                choose_next_pointer(a,b, None)
                return a
            else:
                choose_next_pointer(a,b, None)
                return b

        elif list1:
            return list1
        elif list2:
            return list2
        else:
            return None

        
            
