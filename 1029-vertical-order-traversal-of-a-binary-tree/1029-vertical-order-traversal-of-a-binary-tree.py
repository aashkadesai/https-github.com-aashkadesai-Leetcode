# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        mpp = defaultdict(list)
        if not root:
            return None
        q = deque()
        q.append((root, 0, 0))

        while q:
            node, row, col = q.popleft()
            mpp[col].append((row, node.val))
            if node.left:
                q.append((node.left, row + 1, col - 1))
            if node.right:
                q.append((node.right, row + 1, col + 1))
        
        for col in sorted(mpp.keys()):
            col_vals = sorted(mpp[col], key=lambda x:(x[0], x[1]))
            ans.append([val for row, val in col_vals])
        
        return ans
