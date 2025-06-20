class Solution:
    def longestCommonPrefix(self, s: str, t: str) -> int:
        one_removed = False
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else :
                if not one_removed and i + 1 < len(s) and s[i + 1] == t[j]:
                    one_removed = True
                    i += 2
                    j += 1
                else:
                    break

        return j
            