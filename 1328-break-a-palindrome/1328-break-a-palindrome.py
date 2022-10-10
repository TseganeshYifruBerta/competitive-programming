class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1: return ''
        ans = ''
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                ans = i
                break
        if ans == '':
            return palindrome[:len(palindrome) - 1] + 'b'
        return palindrome[:ans] + 'a' + palindrome[ans + 1:]
                