class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @lru_cache(None)
        def dp(nn, summ):
            if nn == 0:
                if summ == target:
                    return 1
                return 0
            total = 0
            for i in range(1, k + 1):
                total += dp(nn - 1, summ + i)
            return total
        return dp(n, 0) % ((10**9) + 7)
                