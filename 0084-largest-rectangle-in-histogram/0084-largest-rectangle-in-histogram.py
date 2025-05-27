class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        def left_bounds(heights):
            n = len(heights)
            left = [0] * n
            stack = []

            for i in range(n):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                left[i] = stack[-1] + 1 if stack else 0
                stack.append(i)

            return left

        def right_bounds(heights):
            n = len(heights)
            right = [0] * n
            stack = []

            for i in reversed(range(n)):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                right[i] = stack[-1] - 1 if stack else n - 1
                stack.append(i)

            return right

        left = left_bounds(heights)
        right = right_bounds(heights)

        max_area = 0
        for i in range(len(heights)):
            width = right[i] - left[i] + 1
            max_area = max(max_area, heights[i] * width)

        return max_area

        # max_area = 0
        # st = []

        # for i, h in enumerate(heights):
        #     start = i
        #     while st and st[-1][1] > h:
        #         idx, height = st.pop()
        #         max_area = max(max_area, height * (i - idx))
        #         start = idx
        #     st.append((start, h))

        # for i, h in st:
        #     max_area = max(max_area, h * (len(heights) - i))
        
        # return max_area