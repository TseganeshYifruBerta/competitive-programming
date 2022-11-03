class Solution:
    def isMatch(self, st: str, pattern: str) -> bool:
        cache = {}

        def solve(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if  i >= len(st) and j >= len(pattern):
                return True
            if j >= len(pattern):
                return False
            if i >= len(st):
                if pattern[j] == "*":
                    cache[(i, j)] = solve(i, j+1)
                else:
                    cache[(i, j)] = False
            elif pattern[j] == "?":
                cache[(i, j)] = solve(i+1, j+1)
            elif pattern[j] == "*":
                option1 = solve(i, j+1) # match empty string
                option2 = solve(i+1, j+1) # match to any single character
                option3 = solve(i+1, j) # continue matching to  multiple characters
                cache[(i, j)] = option1 or option2 or option3
            else:
                if pattern[j] == st[i]:
                    cache[(i, j)] = solve(i+1, j+1)
                else:
                    cache[(i, j)] = False
            return cache[(i, j)]

        return solve(0, 0)