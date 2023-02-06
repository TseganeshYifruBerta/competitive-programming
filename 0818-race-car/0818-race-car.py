# class Solution:
#     def dp(self, target, curpos, memo, speed):
#         if (curpos, speed) in memo:
#             return memo[(curpos, speed)]
#         if curpos == target:
#             return 0
        
#         forward = inf
#         backward = inf
#         diff = target - curpos
#         temp_speed = -1 if speed > 0 else 1  
        
        
#         if curpos < target and diff >= speed:
#             forward = 1 + self.dp(target, curpos + speed, memo, speed*2)
            
#         elif curpos < target and diff < speed:
#             forward = 1 + self.dp(target, curpos + speed, memo, speed*2)
            
#             backward = 1 + self.dp(curpos, target, memo, temp_speed)
            
#         elif curpos > target:
            
#             backward = 1 + self.dp(curpos, target, memo, temp_speed)
            
        
#         memo[(curpos, speed)] = min(forward, backward)
#         return min(backward,forward)
    
#     def racecar(self, target: int) -> int:
#         return self.dp(target, 0, {}, 1)
        
    
    
    
class Solution:
    def racecar(self, target: int) -> int:
        
        if target == 0:
            return 0
        
        
        dp = [inf] * (target + 1)
        dp[0] = 0
        
        for i in range(1, target+1):
            
            a = 1
            cur_pos = 2 ** a - 1
            
            while cur_pos < i:
                b = 0
                shift = 2**b - 1
                while shift < cur_pos:
                    dp[i] = min(dp[i], a + 1 + b + 1 + dp[i-(cur_pos-shift)])
                    b += 1
                    shift = 2 ** b - 1
                    
                a += 1  
                cur_pos = 2 ** a - 1
                    
                    
            if cur_pos == i:
                
                dp[i] = min(dp[i], a)
                
            elif cur_pos > i:
                dp[i] = min(dp[i], a + 1 + dp[cur_pos - i])

        return dp[target]