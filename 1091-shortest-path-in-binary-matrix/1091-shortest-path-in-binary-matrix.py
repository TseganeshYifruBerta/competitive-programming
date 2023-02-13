class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def inbound(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                return True

        if grid[0][0] != 0: return -1
        q = deque([(-1 ,0, 0)])
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        while q:
            move, row, col = q.popleft()
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return -move
            

            visited.add((row, col))
            for r, c in directions:
                new_r = r + row
                new_c = c + col
                if (new_r, new_c) not in visited and inbound(new_r, new_c) and grid[new_r][new_c] == 0:
                    visited.add((new_r, new_c))
                    q.append((move - 1, new_r, new_c))

        return -1

