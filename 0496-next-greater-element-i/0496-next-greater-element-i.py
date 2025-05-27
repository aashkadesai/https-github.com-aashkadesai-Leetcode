class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        ans = []

        for num in nums2:
            while stack and stack[-1] < num:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)
        
        for num in stack:
            next_greater[num] = -1
        
        for num in nums1:
            ans.append(next_greater[num])
        
        return ans
        
