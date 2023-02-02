class Solution:
    def numberOfWays(self, s: str) -> int:
        left = [[0, 0] for i in range(len(s))]
        right = [[0, 0] for i in range(len(s))]
        
        
#         prefix sum
        for idx in range(len(s)):
            if s[idx] == '0':
                left[idx][0] += 1
            else:
                left[idx][1] += 1
                
            if idx > 0:
                    left[idx][0] += left[idx - 1][0]
                    left[idx][1] += left[idx - 1][1]
            
#       suffix sum
        for idx in range(len(s) - 1, -1, -1):
            if s[idx] == '0':
                right[idx][0] += 1                
            else:
                right[idx][1] += 1
                
            if idx < len(s) - 1:
                    right[idx][0] += right[idx + 1][0]
                    right[idx][1] += right[idx + 1][1]
                    
        answer = 0
        
        for i in range(1, len(s) - 1):
            if s[i] == '0':
                answer += left[i - 1][1] * right[i + 1][1]
                
            if s[i] == '1':
                answer += left[i - 1][0] * right[i + 1][0]
        
        return answer
        
        