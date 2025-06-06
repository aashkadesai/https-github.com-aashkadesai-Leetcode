class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)

        if numRows == 1 or n <= numRows:
            return s

        rows = [""] * numRows
        current_row = 0
        going_down = True

        for ch in s:
            rows[current_row] += ch

            if current_row == 0:
                going_down = True
            elif current_row == numRows - 1:
                going_down = False
            
            current_row += 1 if going_down else -1

        return "".join(rows)