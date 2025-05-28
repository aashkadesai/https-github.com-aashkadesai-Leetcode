from typing import List

class Solution:
    # Directions: Up, Down, Left, Right
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Given a grid with '1' as land and '0' as water, 
        count the number of islands using DFS.
        """
        if not grid:
            return 0  

        self.rows = len(grid)
        self.cols = len(grid[0])
        visited = set()
        island_count = 0

        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    island_count += 1  
                    self.dfs(i, j, grid, visited)
        
        return island_count

    def dfs(self, row: int, col: int, grid: List[List[str]], visited: set):
        if (row < 0 or col < 0 or row >= self.rows or col >= self.cols or grid[row][col] == "0" or (row, col) in visited):
            return

        visited.add((row, col))

        for k in range(4):
            new_row = row + self.dx[k]
            new_col = col + self.dy[k]
            self.dfs(new_row, new_col, grid, visited)

