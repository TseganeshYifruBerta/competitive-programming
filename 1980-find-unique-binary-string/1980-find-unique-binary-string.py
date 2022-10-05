class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def generate(remain):
            if remain == 0:
                return ['']
            lst = generate(remain - 1)
            zero = lst.copy()
            for i in range(len(zero)):
                zero[i] = zero[i] + '0'
            one = lst.copy()
            for i in range(len(one)):
                one[i] = one[i] + '1'
            return zero + one
        lst = generate(len(nums[0]))
        sett = set(nums)
        
        for i in lst:
            if i not in sett:
                return i
        
        
            
            
            