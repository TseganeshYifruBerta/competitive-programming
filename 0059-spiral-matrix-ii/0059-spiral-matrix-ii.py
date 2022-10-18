class Solution:
    def inBound(self, row, col, n):
        if 0 <= row < n and 0 <= col < n:
            return True
        return False
    
    def buildgrid(self, n):
        grid = []
        for row in range(n):
            temp = [0] * n
            grid.append(temp)
        return grid
    
    def changeDir(self, directions):
        return directions[1:] + directions[:1]
    
    
        
        
    def generateMatrix(self, n: int) -> List[List[int]]:
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(grid, row, col, count):
            grid[row][col] = count
            
            for dr, dc in self.directions:
                next_row = dr + row
                next_col = dc + col
#                 if next position is inbound and it's not visited, update
                if self.inBound(next_row, next_col, n) and grid[next_row][next_col] == 0:
                    dfs(grid, next_row, next_col, count + 1)
#                 keep the spiral directions order
                self.directions = self.directions[1:] + self.directions[:1]
        
        grid = self.buildgrid(n)
        dfs(grid, 0, 0, 1)
        return grid