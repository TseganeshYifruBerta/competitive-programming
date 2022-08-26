class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        powerOfTwo, sett, p = set(), set(), 0
        temp = [i for i in str(n)]
        perm = permutations(temp)
        for i in list(perm):
            if i[0] != '0':
                sett.add(int(''.join(i)))
        while p < 30:
            powerOfTwo.add(2**p)
            p += 1
        for i in powerOfTwo:
            if i in sett:
                return True
        return False
            