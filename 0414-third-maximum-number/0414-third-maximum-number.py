class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        nums.reverse()
        maxx = nums[0]
        k = 2
        for i in range(1,len(nums)):
            if nums[i] != maxx:
                maxx = nums[i]
                k -= 1
            if k == 0:
                return maxx
        return nums[0]
            
            