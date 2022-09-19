class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n = num1 + "*" + num2
        n = eval(n)
        return str(n)