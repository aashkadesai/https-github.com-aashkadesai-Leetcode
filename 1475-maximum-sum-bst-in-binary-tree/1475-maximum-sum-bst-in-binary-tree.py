# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        # self.max_sum = 0
         
        # def is_valid(node, low, high):
        #     if not node:
        #         return True
        #     if not (low < node.val < high):
        #         return False
        #     return is_valid(node.left, low, node.val) and is_valid(node.right, node.val, high)
        
        # def sumSubTree(node):
        #     if not node:
        #         return 0
        #     return node.val + sumSubTree(node.left) + sumSubTree(node.right)
        
        # def traverse(node):
        #     if not node:
        #         return None
        #     if is_valid(node, float('-inf'), float('inf')):
        #         subtree_sum = sumSubTree(node)
        #         self.max_sum = max(self.max_sum , subtree_sum)
        #     traverse(node.left)
        #     traverse(node.right)
        
        # traverse(root)
        # return self.max_sum

        self.max_sum = 0

        def helper(node):
            if not node:
                return True, float('inf'), float('-inf'), 0
            
            left_bst, left_min, left_max, left_sum = helper(node.left)
            right_bst, right_min, right_max, right_sum = helper(node.right)

            if left_bst and right_bst and left_max < node.val < right_min:
                total_sum = node.val + left_sum + right_sum
                self.max_sum = max(self.max_sum, total_sum)
                return True, min(left_min, node.val), max(right_max, node.val), total_sum
            else:
                return False, 0, 0, 0

        helper(root)
        return self.max_sum