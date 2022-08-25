class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = Counter(magazine)
        r = Counter(ransomNote)
        for i in r:
            if i not in m:
                return False
            if m[i] < r[i]:
                return False
        return True