class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        visited = [[False] * cols for _ in range(rows)]
        min_heap = [(0,0,0)]

        while min_heap:
            effort, x, y = heapq.heappop(min_heap)
            if x == rows - 1 and y == cols - 1:
                return effort
            if visited[x][y]:
                continue
            visited[x][y] = True
            directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

            for dx, dy in directions:
                nx, ny = dx + x, dy + y
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                    new_eff = max(effort, abs(heights[x][y] - heights[nx][ny]))
                    heapq.heappush(min_heap, (new_eff, nx, ny))

