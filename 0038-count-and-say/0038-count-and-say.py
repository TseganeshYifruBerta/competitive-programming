class Solution:
    def say(self, remain: int) -> str:
        if remain == 1:
            return '1'
        
        result = self.say(remain - 1)
        answer = ''
        count = 0
        temp = result[0]
        for char in result:
            if char != temp:
                answer += str(count) + temp
                count = 0
                temp = char
            count += 1
        answer += str(count) + temp
        return answer
    
    
    def countAndSay(self, n: int) -> str:
        answer = self.say(n)
        return answer
        