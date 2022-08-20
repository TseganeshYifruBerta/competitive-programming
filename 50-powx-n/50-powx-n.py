class Solution:
    def myPow(self, x: float, n: int) -> float:
        @lru_cache(None)
        def rec(n):
            if n <= 1:
                return x
            if n % 2:
                return rec(n // 2) * rec(n // 2) * x
            return rec(n // 2) * rec(n // 2)
        if n == 0: return 1
        if n < 0: return 1/rec(-n)
        return rec(n)