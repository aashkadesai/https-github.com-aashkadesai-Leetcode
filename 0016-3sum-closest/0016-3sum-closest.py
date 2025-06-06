class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = float('inf')

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum
                
                if curr_sum < target:
                    left += 1

                elif curr_sum > target:
                    right -= 1
                
                else:
                    return target
        
        return closest
 

