class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        dr = {}
        dc = {}
        summ = 0
        for row in range(len(grid)):
            dr[row] = max(grid[row])
        p = 0
        while p < len(grid):
            maxx = 0
            for i in range(len(grid)):
                maxx = max(maxx, grid[i][p])
            dc[p] = maxx
            p += 1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                minn = min(dr[row], dc[col])
                summ += minn - grid[row][col]
        return summ
                