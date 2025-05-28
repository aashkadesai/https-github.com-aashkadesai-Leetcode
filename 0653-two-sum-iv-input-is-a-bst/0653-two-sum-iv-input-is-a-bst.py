# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        
        nums = inorder(root)

        l, r = 0, len(nums) - 1
        while l < r:
            curr_sum = nums[l] + nums[r]
            if curr_sum == k:
                return True
            elif curr_sum < k:
                l += 1
            else:
                r -= 1
        return False


        # seen = set()
        # def dfs(node):
        #     if not node:
        #         return False
        #     if (k - node.val) in seen:
        #         return True
        #     seen.add(node.val)
        #     return dfs(node.left) o dfs(node.right)
        # return dfs