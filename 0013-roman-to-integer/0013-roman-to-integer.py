class Solution:
    def romanToInt(self, s: str) -> int:
        romanInt = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev = ''

        for i, ch in enumerate(s):
            if i > 0:
                if romanInt[ch] > romanInt[prev]:
                    total += romanInt[ch] - 2 * romanInt[prev]
                else:
                    total += romanInt[ch] 
            else: 
                total += romanInt[ch] 
            prev = ch
        return total
            