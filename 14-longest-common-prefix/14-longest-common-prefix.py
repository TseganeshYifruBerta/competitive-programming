class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first, last = strs[0], strs[-1]
        f, l = 0, 0
        answer = ''
        while f < len(first) and l < len(last) and first[f] == last[l]:
            answer += first[f]
            f += 1
            l += 1
        return answer