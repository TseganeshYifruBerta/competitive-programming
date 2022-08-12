class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        seen = set()
        self.ans = 0
        def dfs(row, col):
            seen.add((row, col))
            for r, c in dirs:
                new_r = r + row
                new_c = c + col
                if not 0 <= new_r < len(grid) or \
                not 0 <= new_c < len(grid[0]) or grid[new_r][new_c] == 0:
                    self.ans += 1
                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0])\
                and grid[new_r][new_c] == 1 and (new_r, new_c) not in seen:
                    
                    dfs(new_r, new_c)
        
        flag= False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    flag = True
                    break
            if flag: break
        dfs(row, col)
        
        return self.ans
        