class Solution:
    def calculate(self, s: str) -> int:
        postFix = []
        d = {'+' : 0, '-' : 0, '/' : 1, '*': 1}
        stack = []
        p = 0
        while p < len(s):
            if s[p] != ' ':
                if s[p] not in d:
                    t = ''
                    while p < len(s) and s[p] != ' ' and s[p] not in d:
                        t += s[p]
                        p += 1
                    postFix.append(t)
                elif not stack or d[stack[-1]] < d[s[p]]:
                    stack.append(s[p])
                    p += 1
                elif d[stack[-1]] >= d[s[p]]:
                    while stack and d[stack[-1]] >= d[s[p]]:
                        popped = stack.pop()
                        postFix.append(popped)
                    stack.append(s[p])
                    p += 1
            else:
                p += 1
        for i in reversed(range(len(stack))):
            postFix.append(stack[i])
        stack = []
        for i in postFix:
            if i in d:
                first = stack.pop()
                second = stack.pop()
                res = floor(eval(second + i + first))
                stack.append(str(res))
            else:
                stack.append(i)
        return stack[0]
                
        
                