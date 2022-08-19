class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = dict(Counter(nums))
        freq = list(count.items())
        freq.sort()
        memo = {}
        def dp(take):
            if take >= len(freq):
                return 0
            if take == len(freq) - 1:
                return freq[-1][0] * freq[-1][1]
            if take not in memo:
                if freq[take + 1][0] - freq[take][0] > 1:
                    memo[take] = freq[take][0] * freq[take][1] + dp(take + 1) 
                else:
                    memo[take] = max(freq[take][0] * freq[take][1] + dp(take + 2), dp(take + 1))
            return memo[take]
        return dp(0)
                