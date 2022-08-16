class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(list)
        for i in range(len(s)):
            d[s[i]].append(i)
        for i in d:
            if len(d[i]) == 1:
                return d[i][0]
        return -1
            