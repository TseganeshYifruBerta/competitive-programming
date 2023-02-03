class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPal(left, right):
            while right >= left:
                if s[right] != s[left]:
                    return False
                left += 1
                right -= 1
            return True
        
        left, right, res = 0, len(s) - 1, [0, 0]
        while right >= left:
            if s[left] != s[right]:
                res = [left, right]
                break
            left += 1
            right -= 1
            
        return isPal(res[0] + 1, res[1]) or isPal(res[0], res[1] - 1)
                