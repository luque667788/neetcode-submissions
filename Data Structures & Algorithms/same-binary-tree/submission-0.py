# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None:
            return True

        if p is None:
            return False
        if q is None:
            return False

        p_queue = deque([p])
        q_queue = deque([q])
        equal = True
        while p_queue and q_queue:
            p_node = p_queue.popleft()
            q_node = q_queue.popleft()
            if p_node.val != q_node.val:
                equal = False
            else:
                if p_node.right and q_node.right:
                    p_queue.append(p_node.right)
                    q_queue.append(q_node.right)
                elif p_node.right is None and q_node.right is None:
                    pass # reach an end of the node
                else:
                    # one of them is None while the other isnt
                    equal = False

                if p_node.left and q_node.left:
                    p_queue.append(p_node.left)
                    q_queue.append(q_node.left)
                elif p_node.left is None and q_node.left is None:
                    pass # reached an end of the node
                else:
                    # one of them is None while the other isnt

                    equal = False
        return equal
                

                    

        