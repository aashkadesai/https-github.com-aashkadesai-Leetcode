# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st = []
        curr = root
        ct = 0

        while curr or st:
            while curr:
                st.append(curr)
                curr = curr.left
            
            curr = st.pop()
            ct += 1
            if ct == k:
                return curr.val
            curr = curr.right