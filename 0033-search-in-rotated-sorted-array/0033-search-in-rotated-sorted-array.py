class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        left, right = 0, n - 1
         
        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            if nums[middle] >= nums[left]:  # left portion
                if target > nums[middle] or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:   # right portion
                if target < nums[middle] or target > nums[right]:
                    right = middle - 1
                else:
                    left = middle + 1
        return -1