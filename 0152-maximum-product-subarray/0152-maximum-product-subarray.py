class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # res = m,ax(nums)
        # curMax, curMin = 1, 1

        # for n in nums:

        #     tmp = curMax * n
        #     curMax = max(curMin * n, curMax * n, n) #[-1, 8]
        #     curMin = min(curMin * n, tmp, n) #[-1, -8]

        #     res = max(res, curMax)

        pref, suff = 1, 1
        n = len(nums)
        res = float('-inf')

        for i in range(n):
            if pref == 0:
                pref = 1
            if suff == 0:
                suff = 1
            pref = pref * nums[i]
            suff = suff * nums[n - i -1]
            res = max(res, max(pref, suff))

        return res