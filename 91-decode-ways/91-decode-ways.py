class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def dp(idx):
#             basecases
            if idx >= len(s): return 1
            if s[idx] == '0': return 0
#          if peeking two digits is invalid their has to be default value
            two = 0
            
#             peeking one digit is always valid b/c the value doesn't exceed 9
            one = dp(idx + 1)
    
#     peeking two digits if it is valid
            if idx + 1 < len(s) and int(s[idx] + s[idx + 1]) <= 26:
                two = dp(idx + 2)
            
#             return the summation
            return one + two
        return dp(0)