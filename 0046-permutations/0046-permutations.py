class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)

        def helper():

            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                helper()
                path.pop()
                used[i] = False
            
        helper()
        return res