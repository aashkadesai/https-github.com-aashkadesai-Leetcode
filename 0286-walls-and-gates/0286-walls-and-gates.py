class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return 0
        
        INF = 2147483647
        rows, cols = len(rooms), len(rooms[0])
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    q.append((i, j))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < rows and 0 <= new_y < cols and rooms[new_x][new_y] == INF:
                    rooms[new_x][new_y] = rooms[x][y] + 1
                    q.append((new_x, new_y))
        return rooms

