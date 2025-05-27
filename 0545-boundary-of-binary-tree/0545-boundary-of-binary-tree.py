# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        def is_leaf(node):
            return not node.left and not node.right
        
        def addLeftBoundary(node):
            while node:
                if not is_leaf(node):
                    boundary.append(node.val)
                if node.left:
                    node = node.left
                else:
                    node = node.right
        
        def addRightBoundary(node):
            temp = []
            while node:
                if not is_leaf(node):
                    temp.append(node.val)
                if node.right:
                    node = node.right
                else:
                    node = node.left
            boundary.extend(temp[::-1])
        
        def addLeaves(node):
            if is_leaf(node):
                boundary.append(node.val)
                return
            if node.left:
                addLeaves(node.left)
            if node.right:
                addLeaves(node.right)
                    
        boundary = []
        if not is_leaf(root):
            boundary.append(root.val)
        addLeftBoundary(root.left)
        addLeaves(root)
        addRightBoundary(root.right)
    
        return boundary
