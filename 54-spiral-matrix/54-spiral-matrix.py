class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        self.ans = [matrix[0][0]]
        def dfs(row, col):
            visited.add((row, col))
            for r, c in self.dirs:
                new_r = r + row
                new_c = c + col
                if 0 <= new_r < len(matrix) and \
                0 <= new_c < len(matrix[0]) and (new_r, new_c) not in visited:
                    self.ans.append(matrix[new_r][new_c])
                    dfs(new_r, new_c)
                self.dirs = self.dirs[1:] + self.dirs[:1]
        dfs(0, 0)
        return self.ans
        
        
        