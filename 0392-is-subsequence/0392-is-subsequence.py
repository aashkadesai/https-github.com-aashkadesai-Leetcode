class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        f = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    f[i][j] = 1 + f[i - 1][j - 1]
                else:
                    f[i][j] = max(f[i - 1][j], f[i][j - 1])

        if f[m][n] == m:
            return True

        return False