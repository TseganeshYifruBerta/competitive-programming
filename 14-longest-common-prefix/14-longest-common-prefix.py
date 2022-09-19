class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first, last = strs[0], strs[-1]
        p = 0
        while p < len(first) and p < len(last) and first[p] == last[p]:
            p += 1
        return first[:p]