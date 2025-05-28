class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_pal(substr):
            return substr == substr[::-1]
        
        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                pre = s[start:end]
                if is_pal(pre):
                    path.append(pre)
                    backtrack(end, path)
                    path.pop()
        backtrack(0, [])
        return res