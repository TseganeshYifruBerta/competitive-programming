class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        M = [10**9+7]
        dp = {}
        def helper(start, rem):
            if rem == 0:
                if  start == endPos:
                    return 1
                return 0
            if (start, rem) not in dp:
                left, right = 0, 0
                if rem >= abs(endPos - start):
                    left = helper(start - 1, rem - 1)
                    right = helper(start + 1, rem - 1)
                dp[(start, rem)] = left + right
            return dp[(start, rem)] % M[0]
        
        return helper(startPos, k)