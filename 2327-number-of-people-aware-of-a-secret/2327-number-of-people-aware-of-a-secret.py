class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        @lru_cache(None)
        def dp(day):
            if day > n:
                return 0
            count = 0 if day + forget <= n else 1
            for i in range(day + delay, forget + day):
                count += dp(i)
            return count % (((10)**9) + 7)
        
        
        return dp(1) % (((10)**9) + 7)
                    