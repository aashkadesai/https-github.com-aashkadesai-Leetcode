class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)
        dp = [[False] * n for _ in range(n)]

        for length in range(1, n + 1):  
            for i in range(n - length + 1):
                j = i + length - 1
                substring = s[i:j+1]

                if substring in word_set:
                    dp[i][j] = True
                    continue

                for k in range(i, j):
                    if dp[i][k] and dp[k+1][j]:
                        dp[i][j] = True
                        break

        return dp[0][n - 1]