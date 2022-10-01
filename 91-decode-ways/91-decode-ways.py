class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def dp(idx):
            if idx >= len(s): return 1
            if s[idx] == '0': return 0
            one, two = 0, 0
            one = dp(idx + 1)
            if idx + 1 < len(s) and int(s[idx] + s[idx + 1]) <= 26:
                two = dp(idx + 2)
            return one + two
        return dp(0)