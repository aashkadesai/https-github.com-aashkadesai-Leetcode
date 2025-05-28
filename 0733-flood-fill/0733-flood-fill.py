class Solution:
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])

        org_color = image[sr][sc]

        if org_color == color:
            return image

        self.dfs(sr, sc, org_color, color, image, row, col)

        return image

    def dfs(self, i, j, org_color, color, image, row, col):
        if i < 0 or j < 0 or i >= row or j >= col or image[i][j] != org_color:
            return 

        image[i][j] = color

        for k in range(4):
            ii = i + self.dx[k]
            jj = j + self.dy[k]

            self.dfs(ii, jj, org_color, color, image, row, col)

