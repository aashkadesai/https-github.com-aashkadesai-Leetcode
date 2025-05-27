# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float('-inf')]
        self.diameterOfBinaryTree(root, res)
        return res[0]

    def diameterOfBinaryTree(self, root, res):
        if not root:
            return 0
        left = self.diameterOfBinaryTree(root.left, res)
        right = self.diameterOfBinaryTree(root.right, res)
        temp = max(max(left, right) + root.val, root.val)
        ans = max(temp, root.val + left + right)
        res[0] = max(ans, res[0])
        return temp