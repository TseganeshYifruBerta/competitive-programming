class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPal(l, r):
            while r >= l:
                if s[r] != s[l]:
                    return False
                l += 1
                r -= 1
            return True
        
        l, r, res = 0, len(s) - 1, [0, 0]
        while r >= l:
            if s[l] != s[r]:
                res = [l, r]
                break
            l += 1
            r -= 1
            
        return isPal(res[0] + 1, res[1]) or isPal(res[0], res[1] - 1)
                