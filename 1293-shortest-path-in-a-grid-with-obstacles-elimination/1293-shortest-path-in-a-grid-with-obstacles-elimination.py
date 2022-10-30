class Solution:
    def inBound(self, row, col, m, n):
        if 0 <= row <= m and 0 <= col <= n:
            return True
        return False
                
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = deque([(0, 0, 0, k)])
        m = len(grid) - 1
        n = len(grid[0]) - 1
        visited = set()
        
        
#         
        while q:
            steps, row, col, remain = q.popleft()
            
            if row == m and col == n:
                return steps
            visited.add((row, col, remain))
            
            for r, c in directions:
                new_r = row + r
                new_c = col + c
                if self.inBound(new_r, new_c, m, n):
                    if grid[new_r][new_c] == 1 and remain > 0:
                        if (new_r, new_c, remain - 1) not in visited:
                            visited.add((new_r, new_c, remain - 1))
                            q.append((steps + 1, new_r, new_c, remain - 1))
                            
                    elif grid[new_r][new_c] == 0:
                        if (new_r, new_c, remain) not in visited:
                            visited.add((new_r, new_c, remain))
                            q.append((steps + 1, new_r, new_c, remain))
        return -1
                    
                    
            