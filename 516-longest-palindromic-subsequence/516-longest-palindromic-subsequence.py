class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def dp(l, r):
            if r < l:
                return 0
            count = 0
            if s[l] == s[r]:
                count = dp(l + 1, r - 1)
                count = count + 1 if l == r else count + 2
                
            else:
                left = dp(l + 1, r)
                right = dp(l, r - 1)
                count = max(left, right)
            return count
        return dp(0, len(s) - 1)
                
            
            
            
        