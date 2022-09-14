class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        freq_s = Counter(s)
        freq_t = Counter(t)
        for i in freq_t:
            if i not in freq_s or freq_t[i] != freq_s[i]:
                return False
        return True
            
        
        