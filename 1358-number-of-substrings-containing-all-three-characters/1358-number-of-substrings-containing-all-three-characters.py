class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d = defaultdict(int)
        p1, p2 = 0, 0
        total = 0
        while p2 < len(s):
            if d['a'] >= 1 and d['b'] >= 1 and d['c'] >= 1:
                total += 1 + len(s) - p2
                d[s[p1]] -= 1
                p1 += 1
            else:
                d[s[p2]] += 1
                p2 += 1
        
        while p1 < len(s):
            if d['a'] >= 1 and d['b'] >= 1 and d['c'] >= 1:
                total += 1
                d[s[p1]] -= 1
                p1 += 1
            else:
                return total
        return total
                
            