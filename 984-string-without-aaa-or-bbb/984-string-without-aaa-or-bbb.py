class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        def helper(f, s, g):
            res = []
            gg = [g[0] * 2, g[0], g[1] * 2, g[1]]
            while f != 0 or s != 0:
                if f - s >= 2 and s !=0 and f != 0:
                    res.append(gg[0])
                    res.append(gg[3])
                    f -= 2
                    s -= 1
                    continue
                if f >= 2:
                    res.append(gg[0])
                    f -= 2
                elif f == 1:
                    res.append(gg[1])
                    f -= 1
                if s >= 2:
                    res.append(gg[2])
                    s -= 2
                elif s == 1:
                    res.append(gg[3])
                    s -= 1
            return "".join(res)
        if a > b:
            res = helper(a, b, ("a", "b"))
        else:
            res = helper(b, a, ("b", "a"))
        return res