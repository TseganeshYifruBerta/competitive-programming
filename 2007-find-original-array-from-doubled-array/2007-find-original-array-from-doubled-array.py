class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0: return []
        count = Counter(changed)
        changed.sort()
        
        ans = []
        for i in changed:
            if count[i] > 0:
                count[i] -= 1
                if i * 2 in count and count[i * 2] > 0:
                    ans.append(i)
                    count[i * 2] -= 1
        if len(ans) == len(changed) // 2:
            return ans
        return []
        
        
        
        