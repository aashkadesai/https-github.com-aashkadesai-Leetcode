class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1 = len(word1)
        w2 = len(word2)
        t = [[0] * (w2 + 1) for _ in range(w1 + 1)]

        for i in range(w1 + 1):
            t[i][0] = i  
        for j in range(w2 + 1):
            t[0][j] = j

        for i in range(1, w1 + 1):
            for j in range(1, w2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    t[i][j] = t[i - 1][j - 1]
                else:
                    insert = t[i][j - 1] + 1
                    delete = t[i - 1][j] + 1
                    replace = t[i - 1][j - 1] + 1
                    t[i][j] = min(insert, delete, replace)
        return t[w1][w2]

        
