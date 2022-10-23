class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        lost = None
        duplicate = None
        set_duplicate = set()
        for i in range(len(nums)):
            if nums[i] not in set_duplicate:
                set_duplicate.add(nums[i])
            else:
                duplicate = nums[i]
        
        for i in range(1, len(nums) + 1):
            if i not in set_duplicate:
                lost = i
                
        return [duplicate, lost]