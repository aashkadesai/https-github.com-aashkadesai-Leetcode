class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        t  = [[0] * n for _ in range(m)]

        t[0][0] = grid[0][0]

        for i in range(1, m):
            t[i][0] = t[i - 1][0] + grid[i][0]
            
        for j in range(1, n):
            t[0][j] = t[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                t[i][j] = min(t[i - 1][j], t[i][j - 1])+ grid[i][j]
        
        return t[m - 1][n - 1]