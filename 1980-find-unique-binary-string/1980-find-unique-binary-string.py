class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def generate(remain):
            if remain == 0:
                return ['']
            lst = generate(remain - 1)
            l = []
            for i in range(len(lst)):
                l.append(lst[i] + '0')
                l.append(lst[i] + '1')
            return l
        
        lst = generate(len(nums[0]))
        sett = set(nums)
        
        for i in lst:
            if i not in sett: return i
        
        
            
            
            