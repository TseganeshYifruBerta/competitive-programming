class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def rec(n):
            if n == 0:
                return False
            if n == 1:
                return True
            if n % 4:
                return False
            return rec(n // 4)
        return rec(n)