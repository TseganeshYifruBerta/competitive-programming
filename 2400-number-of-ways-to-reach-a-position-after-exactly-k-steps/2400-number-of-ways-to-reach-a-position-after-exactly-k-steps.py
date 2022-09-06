class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        M = [10**9+7]
        @lru_cache(None)
        def helper(start, rem):
            if rem == 0:
                if  start == endPos:
                    return 1
                return 0
            left = helper(start - 1, rem - 1)
            right = helper(start + 1, rem - 1)
            return (left  + right) % M[0]
        return helper(startPos, k)