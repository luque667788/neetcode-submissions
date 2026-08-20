# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = deque([root])
        while stack:
            node = stack.popleft()

            if node.val < p.val and node.val < q.val:
                if node.right:
                    stack.append(node.right)
            elif node.val > p.val and node.val > q.val:
                if node.left:
                    stack.append(node.left)
            else:
                # there is a split and we know this is the 
                # lowest node where both of them are child of 
                # it could also be that one is equal
                return node
        return root
