class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        res = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Check for sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Step 3: Convert digits
        while i < n and s[i].isdigit():
            res = res * 10 + int(s[i])

            # Step 4: Clamp if out of bounds
            if sign == 1 and res > INT_MAX:
                return INT_MAX
            if sign == -1 and -res < INT_MIN:
                return INT_MIN

            i += 1

        return sign * res
