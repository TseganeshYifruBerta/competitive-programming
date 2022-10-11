class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def matchPattern(s_idx, p_idx):
            if s_idx >= len(s) and p_idx >= len(p):
                    return True
            if s_idx >= len(s):
                for idx in range(p_idx, len(p)):
                    if p[idx] != "*":
                        return False
                return True
            if p_idx >= len(p):
                return False
            if 97 <= ord(s[s_idx]) <= 122 and 97 <= ord(p[p_idx]) <= 122:
                if s[s_idx] != p[p_idx]:
                    return False

            first, second, third = False, False, False
            if p[p_idx] == "*":
                first = matchPattern(s_idx, p_idx + 1)
                second = matchPattern(s_idx + 1, p_idx)
            third = matchPattern(s_idx + 1, p_idx + 1)
            return first or second or third
        return matchPattern(0, 0)