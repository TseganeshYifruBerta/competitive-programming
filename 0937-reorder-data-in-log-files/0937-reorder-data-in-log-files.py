class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig = []
        d = defaultdict(list)
        for i in logs:
            l = i.split()
            if 97 <= ord(l[1][0]) <= 122:
                d[l[0]].append(l[1:])
            else:
                dig.append(i)
        lst = []
        for i in d:
            for j in d[i]:
                lst.append((j, i))
        lst.sort()
        ans = []
        for i in lst:
            ans.append(' '.join([i[1]] + i[0]))
        ans += dig
        return ans
                