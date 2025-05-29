class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        events = []
        MOD = 10 ** 9 + 7

        def getArea(width):
            if not intervals:
                return 0
            intervals.sort()
            total = 0
            prev_start, prev_end = intervals[0]
            for start, end in intervals[1:]:
                if start > prev_end:
                    total += prev_end - prev_start
                    prev_start, prev_end = start, end
                else:
                    prev_end = max(prev_end, end)
            total += prev_end - prev_start
            return total * width

        for x1, y1, x2, y2 in rectangles:
            events.append((x1, 0, y1, y2))
            events.append((x2, 1, y1, y2))

        events.sort()
        intervals = []
        ans = 0
        pre_x = 0

        for cur_x, e, y1, y2 in events:
            ans += getArea(cur_x - pre_x)
            ans %= MOD
            
            if e == 1:
                intervals.remove((y1, y2))
            else:
                intervals.append((y1, y2))
            pre_x = cur_x

        return ans
