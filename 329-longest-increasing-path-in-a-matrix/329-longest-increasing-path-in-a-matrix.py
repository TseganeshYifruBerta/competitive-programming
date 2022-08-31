class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def inBound(row, col):
            return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = [0]
        visited = set()
        @cache
        def dfs(row, col):
            if not inBound(row, col):
                return 0
            visited.add((row, col))
            maxx = 0
            for r, c in dirs:
                new_r = row + r
                new_c = col + c
                if inBound(new_r, new_c) and\
                matrix[new_r][new_c] > matrix[row][col]:
                    count = 1 + dfs(new_r, new_c)
                    maxx = max(count, maxx)
            ans[0] = max(ans[0], maxx)
            return maxx
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (row, col) not in visited:
                    dfs(row, col)
        return ans[0] + 1
        