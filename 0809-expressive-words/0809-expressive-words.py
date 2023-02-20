class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def RLE(S):
            return zip(*[(k, len(list(grp))) for k, grp in itertools.groupby(S)])

        R, count = RLE(s)
        ans = 0
        for word in words:
            R2, count2 = RLE(word)
            if R2 != R: continue
            ans += all(c1 >= max(c2, 3) or c1 == c2
                       for c1, c2 in zip(count, count2))

        return ans