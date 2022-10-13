class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        seen = set()
        def inBound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = deque()
        def dfs(row, col):
            q.append(((row, col), 0))
            grid[row][col] = 0
            for r, c in dirs:
                new_r = row + r
                new_c = col + c
                if inBound(new_r, new_c) and grid[new_r][new_c] == 1:
                    dfs(new_r, new_c)
        flag = True
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    flag = False
                    dfs(row, col)
                    break
            if not flag:
                break
        while q:
            cur, step = q.popleft()
            row, col = cur
            seen.add(cur)
            if grid[row][col] == 1:
                return step - 1
            for r, c in dirs:
                new_r = row + r
                new_c = col + c
                if inBound(new_r, new_c) and (new_r, new_c) not in seen:
                    seen.add((new_r, new_c))
                    q.append(((new_r, new_c), step + 1))
                
                    
        
        