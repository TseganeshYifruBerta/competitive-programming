class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate(n):
            n = str(n)
            ans = 0
            for i in n:
                ans += (int(i))**2
            return ans
        sett = set()
        
        while n != 1 and n not in sett:
            sett.add(n)
            n = calculate(n)
        return n == 1