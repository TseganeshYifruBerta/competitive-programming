class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPal(l, r):
            while r >= l:
                if s[r] != s[l]:
                    return False
                l += 1
                r -= 1
            return True
        left, right, flag = 0, len(s) - 1, True
        while right >= left:
            if s[left] != s[right]:
                res = [left, right]
                flag = False
                break
            left += 1
            right -= 1
        if not flag:
            ans1 = isPal(res[0] + 1, res[1])
            ans2 = isPal(res[0], res[1] - 1)
            if ans1 or ans2: 
                return True
            else:
                return False
        return True
                