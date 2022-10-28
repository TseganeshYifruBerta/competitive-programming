class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        d = defaultdict(list)
        for i in strs:
            temp = [0] * 26
            for j in i:
                temp[ord(j) - 97] += 1
            d[tuple(temp)].append(i)
        for i in d:
            ans.append(d[i])
        return ans