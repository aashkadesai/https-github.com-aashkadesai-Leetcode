class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0

        def isPal(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:                   
                r += 1
                l -= 1
            return l + 1, r - 1
        
        for i in range(len(s)):
            l1, r1 = isPal(i, i)
            l2, r2 = isPal(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        
        return s[start : end + 1]

            