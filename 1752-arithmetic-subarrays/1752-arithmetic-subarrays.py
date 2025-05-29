class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []

        for i in range(len(l)):
            new_nums = nums[l[i]:r[i] + 1]
            new_nums.sort()

            diff = new_nums[1] - new_nums[0]
            is_arithmetic = True

            for j in range(2, len(new_nums)):
                if (new_nums[j] - new_nums[j - 1]) != diff:
                    is_arithmetic = False
                    break
            res.append(is_arithmetic)
        
        return res
