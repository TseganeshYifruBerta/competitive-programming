class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        ans = ''
        for i in range(1, len(lst)):
            ans += ' ' + lst[i][::-1]
        ans = lst[0][::-1] + ans
        return ans
            
        