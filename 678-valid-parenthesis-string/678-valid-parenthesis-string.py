class Solution:
    def checkValidString(self, s: str) -> bool:
        @lru_cache(None)
        def helper(idx, opened):
            if idx >= len(s):
                if opened == 0:
                    return True
                return False
            if opened == 0 and s[idx] == ')':
                return False
            if s[idx] == '*':
                u = False
                l = helper(idx + 1, opened)
                r = helper(idx + 1, opened + 1)
                if opened > 0:
                    u = helper(idx + 1, opened - 1)
                return l or u or r
            else:
                if s[idx] == ')':
                    return helper(idx + 1, opened - 1)
                if s[idx] == '(':
                    return helper(idx + 1, opened + 1)
        return helper(0, 0)