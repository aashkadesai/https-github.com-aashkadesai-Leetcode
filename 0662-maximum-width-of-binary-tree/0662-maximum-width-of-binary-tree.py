# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 0
        q = deque()
        q.append((root, 0))

        while q:
            level = len(q)
            _, level_head_index = q[0]

            for _ in range(level):
                node, idx = q.popleft()
                curr_idx = idx - level_head_index
                if node.left:
                    q.append((node.left, 2 * curr_idx))
                if node.right:
                    q.append((node.right, 2 * curr_idx + 1))
        
            if q:
                width = q[-1][1] - q[0][1] + 1
                max_width = max(max_width, width)
            else:
                max_width = max(max_width, 1)
        return max_width
            