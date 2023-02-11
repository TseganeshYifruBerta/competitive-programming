class Solution:
    def isPalindrom(self, start, end, s):
        while start >= 0 and end < len(s) and s[end] == s[start]:
            start -= 1
            end += 1
        return [start + 1, end - 1]


    def longestPalindrome(self, s: str) -> str:
        max_palindrom = 1
        answer = [0, 0]
        
        for center in range(len(s)):
            odd_start, odd_end = self.isPalindrom(center, center, s)
            even_start, even_end = self.isPalindrom(center, center + 1, s)
            odd_len = odd_end - odd_start + 1
            even_len = even_end - even_start + 1
            if odd_len > max_palindrom:
                answer = [odd_start, odd_end]
                max_palindrom = odd_len
            if even_len > max_palindrom:
                answer = [even_start, even_end]
                max_palindrom = even_len
           
                
        return s[answer[0]:answer[1] + 1]