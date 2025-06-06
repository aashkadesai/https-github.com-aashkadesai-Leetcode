class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        low = 0
        high = n - 1

        while low < high:
            mid = (low + high) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                high = mid
        return nums[low]

        