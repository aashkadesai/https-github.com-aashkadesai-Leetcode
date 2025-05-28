# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        def insert(node, val):
            if val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                else:
                    insert(node.left, val)
            else:
                if not node.right:
                    node.right = TreeNode(val)
                else:
                    insert(node.right, val)
        root = TreeNode(preorder[0])

        for val in preorder[1:]:
            insert(root, val)
        
        return root