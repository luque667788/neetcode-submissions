# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def exchange_kids(mother: TreeNode):

            # switch them up
            if mother.left: 
                exchange_kids(mother.left)
            if mother.right:
                exchange_kids(mother.right)

            left = mother.left
            mother.left = mother.right
            mother.right = left

        if not root:
             return None

        exchange_kids(root)
        return root

                


        