from collections import deque
from typing import List

class Solution:
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh_oranges = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        
        minutes = 0

        while q:
            rotten = False
            for _ in range(len(q)):
                row, col = q.popleft()
                for k in range(4):
                    ii, jj = row + self.dx[k], col + self.dy[k]
                    if 0 <= ii < rows and 0 <= jj < cols and grid[ii][jj] == 1:
                        grid[ii][jj] = 2
                        fresh_oranges -= 1
                        rotten = True
                        q.append((ii, jj))
                
            if rotten == True:
                minutes += 1
    
        return minutes if fresh_oranges == 0 else -1


        # rows, cols = len(grid), len(grid[0])
        # q = deque()
        # fresh_oranges = 0

        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == 2:
        #             q.append((i, j))  
        #         elif grid[i][j] == 1:
        #             fresh_oranges += 1  

        # if fresh_oranges == 0:
        #     return 0

        # minutes = 0  

        # while q:
        #     level_size = len(q)
        #     new_rotten = False

        #     for _ in range(level_size):
        #         i, j = q.popleft()

        #         for k in range(4):
        #             ii, jj = i + self.dx[k], j + self.dy[k]

        #             if 0 <= ii < rows and 0 <= jj < cols and grid[ii][jj] == 1:
        #                 grid[ii][jj] = 2  
        #                 q.append((ii, jj))  
        #                 fresh_oranges -= 1  
        #                 new_rotten = True

        #     if new_rotten:  
        #         minutes += 1

        # return minutes if fresh_oranges == 0 else -1

