class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0, 1), (1, 0), (-1, 0), (0,-1)]
        def dfs(row, col):
            # if not 0 <= row < len(grid) or not 0 <= col < len(grid[0]):
            #     return
            for r, c in dirs:
                new_r = r + row
                new_c = c + col
                if 0 <= new_r < len(grid) and \
                0 <= new_c < len(grid[0]) \
                and grid[new_r][new_c] == "1":
                    grid[new_r][new_c] = "0"
                    dfs(new_r, new_c)
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row, col)
        return count
                    