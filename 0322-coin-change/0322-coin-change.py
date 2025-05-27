class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = len(coins)
        n = amount
        INT_MAX = float('inf')

        dp = [[0 if j == 0 else INT_MAX for j in range(n + 1)] for i in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if coins[i - 1] <= j:
                    dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n] if dp[m][n] != INT_MAX else -1