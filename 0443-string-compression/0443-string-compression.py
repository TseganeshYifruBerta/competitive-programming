class Solution:
    def compress(self, chars: List[str]) -> int:
        answer = []
        def insertt(char):
            if char <= 1: return
            for i in str(char):
                answer.append(i)
                
        prev_char, prev_count = chars[0], 1
        
        for i in range(1, len(chars)):
            if chars[i] != prev_char:
                answer.append(prev_char)
                insertt(prev_count)
                prev_count , prev_char = 0, chars[i]
            prev_count += 1
            
        answer.append(prev_char)
        
        insertt(prev_count)
                
        for i in range(len(answer)):
            chars[i] = answer[i]
            
        return len(list(answer))
            
        