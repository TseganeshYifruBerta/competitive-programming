class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        c = Counter(words)
        lst = []
        sett = set()
        ans = []
        for i in c:
            if i not in sett and i[::-1] in c:
                if i[::-1] == i:
                    ans.append(c[i])
                else:
                    lst.append((c[i[::-1]], c[i]))
                sett.add(i)
                sett.add(i[::-1])
        summ = 0
        for l, r in lst:
            summ += 4 * (min(l, r))
        m = 0
        f = 0
        for i in ans:
            if i % 2:
                f = 2
            summ += ((i // 2) * 2) * 2
        return summ + f