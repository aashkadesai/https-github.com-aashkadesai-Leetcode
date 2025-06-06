class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1

        def find_first(left, right, first):
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    first = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first

        def find_last(left, right, last):
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                   last = mid
                   left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last

        return [find_first(left, right, -1), find_last(left, right, -1)]