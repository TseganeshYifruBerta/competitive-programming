class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dp(idx, summ):
            if summ == target and idx == len(nums):
                return 1
            if idx >= len(nums):
                return 0
            neg, pos = 0, 0
            neg = dp(idx + 1, summ - nums[idx])
            pos = dp(idx + 1, summ + nums[idx])
            return neg + pos
        return dp(0, 0)
            