class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:          
        # nums.sort()               
        # result = []

        # length = len(nums)

        # for i in range(length - 2):
        #     if i > 0 and nums[i]==nums[i-1]:
        #         continue

        #     left = i+1
        #     right = length - 1

        #     while left < right:
        #         total = nums[i]+nums[left]+nums[right]
        #         if total < 0:
        #             left += 1
        #         elif total > 0:
        #             right -= 1
        #         else:
        #             result.append([nums[i],nums[left], nums[right]])

        #             while left < right and nums[left]==nums[left+1]:
        #                 left += 1
        #             while left < right and nums[right]==nums[right-1]:
        #                 right -= 1
                    
        #             left = left + 1
        #             right = right - 1
        # return result

        nums.sort()
        res = set()
        target = 0
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = -nums[i]
            seen = set()
            for j in range(i + 1, n):
                comp = target - nums[j]
                if comp in seen:
                    res.add((nums[i], comp, nums[j]))
                seen.add(nums[j])
        
        return list(res)

            
