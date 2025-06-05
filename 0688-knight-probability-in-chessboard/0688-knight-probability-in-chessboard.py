class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(-2, -1), (-2, 1), (2, -1), (2, 1),
                      (-1, -2), (-1, 2), (1, -2), (1, 2)]

        @lru_cache(maxsize=None)
        def dp(k, r, c):
            if r < 0 or c < 0 or r >= n or c >= n:
                return 0
            if k == 0:
                return 1
            
            prob = 0
            for dr, dc in directions:
                prob += dp(k - 1, r + dr, c + dc) / 8
            return prob
        
        return dp(k, row, column)
            