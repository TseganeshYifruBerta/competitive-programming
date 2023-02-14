class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        answer = 0
        
        for i in range(len(s)):
            if stack and s[i] == "a" and stack[-1] == "b":
                stack.pop()
                answer += 1
            else:
                stack.append(s[i])
                
        return answer
