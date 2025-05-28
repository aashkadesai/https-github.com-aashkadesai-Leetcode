class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def helper(start, path, remain):
            if remain == 0:
                res.append(path[:])
                return
            if remain < 0:
                return 
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                helper(i + 1, path, remain - candidates[i])
                path.pop()
        helper(0, [], target)
        return res