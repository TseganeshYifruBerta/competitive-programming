class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
# the whole sum minus the non-duplicated sum gives as the duplicate value
        duplicate = sum(nums) - sum(set(nums))
    
# the arithimetic sum 1 - n
        arth_sum = int((((n + 1) / 2) * n)) 
    
# we can get the lost one by subtracting the non-duplicated to the arth_sum
        lost = arth_sum - sum(set(nums))
        return [duplicate, lost]