class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum = [0 for i in range(len(s) + 1)]
        for start, end, direction in shifts:
            if direction == 0:
                prefix_sum[start] -= 1
                prefix_sum[end + 1] += 1
            else:
                prefix_sum[start] += 1
                prefix_sum[end + 1] -= 1
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i - 1]
        
        answer = []
        for i in range(len(s)):
            cur = chr(((ord(s[i]) - ord('a') + prefix_sum[i])%26) + ord('a'))
            answer.append(cur)
            
        return ''.join(answer)