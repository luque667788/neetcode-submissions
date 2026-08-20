# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        # I believe that this is a classical example of DFS
        # problem is i dont remember the syntax of it
        if root is None:
            return 0

        max_depth = 0
        stack = deque([(root, 1)])
        while stack:
            (node, depth) = stack.popleft()
            max_depth = max(max_depth, depth)
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
        return max_depth
            
            
                