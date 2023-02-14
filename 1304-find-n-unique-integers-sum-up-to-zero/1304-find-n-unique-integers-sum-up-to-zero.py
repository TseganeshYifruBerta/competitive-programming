class Solution:
    def sumZero(self, n: int) -> List[int]:
        left, right = -n, n
        answer = [0] if n % 2 else []
        n = n - 1 if n % 2 else n
        
        while len(answer) < n: 
            answer.append(left)
            answer.append(right)
            right -= 1
            left += 1
            
        return answer