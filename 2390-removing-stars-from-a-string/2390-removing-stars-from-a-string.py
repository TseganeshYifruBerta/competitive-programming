class Solution:
    def removeStars(self, s: str) -> str:
        def func(s):
            stk = []

            for char in s:
                if char == '*':
                    stk.pop()
                    continue

                stk.append(char)

            return "".join(stk)
        
        return func(s)