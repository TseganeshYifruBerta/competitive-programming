class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def isPower(n):
            if n == 1: return True
            if n % 3: return False
            return isPower(n / 3)
        if n == 0 : return False
        return isPower(n)