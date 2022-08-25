class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0: return 0
        s.sort()
        g.sort()
        p, count = 0, 0
        for i in range(len(s)):
            if p < len(g) and s[i] < g[p]:
                continue
            if p >= len(g):
                return len(g)
            count += 1
            p += 1
        return count