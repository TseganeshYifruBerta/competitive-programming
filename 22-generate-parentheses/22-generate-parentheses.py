class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(s):
            stack = []
            for i in s:
                if i == '(':
                    stack.append(i)
                else:
                    if not stack:
                        return False
                    stack.pop()
            return len(stack) == 0
        ans = []
        def generante(s, opened, closed):
            if opened == 0 and closed == 0:
                ans.append(s)
                return 
            if opened > 0:
                generante(s + '(', opened - 1, closed)
            if closed > 0:
                generante(s + ')', opened, closed - 1)
        generante('', n, n)
        res = []
        for i in ans:
            if isValid(i):
                res.append(i)
        return res