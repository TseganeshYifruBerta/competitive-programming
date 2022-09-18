class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def outOfBound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        def dfs(row, col):
            if row >= len(grid):
                return col
            
            
            if grid[row][col] == 1:
                if col + 1 < len(grid[0]) and grid[row][col + 1] == 1:
                    return dfs(row + 1, col + 1)
            if grid[row][col] == -1:
                if col - 1 >= 0 and grid[row][col - 1] == -1:
                    return dfs(row + 1, col - 1)
                
            return -1
        ans = []
        for i in range(len(grid[0])):
            ans.append(dfs(0, i))
        return ans
                    