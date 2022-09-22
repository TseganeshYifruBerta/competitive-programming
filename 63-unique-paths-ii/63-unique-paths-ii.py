class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1:
            return 0
        dp = [[0 for i in range(len(obstacleGrid[0]) + 1)] for j in range(len(obstacleGrid) + 1)]
        dp[-2][-2] = 1
        for row in range(len(obstacleGrid) - 1, -1, -1):
            for col in range(len(obstacleGrid[0]) - 1, -1, -1):
                if obstacleGrid[row][col] == 0:
                    if row + 1 < len(obstacleGrid) and  obstacleGrid[row + 1][col] == 0:
                        dp[row][col] += dp[row + 1][col]
                    if col + 1 < len(obstacleGrid[0]) and obstacleGrid[row][col + 1] == 0:
                        dp[row][col] += dp[row][col + 1]
        print(dp)
        return dp[0][0]
        