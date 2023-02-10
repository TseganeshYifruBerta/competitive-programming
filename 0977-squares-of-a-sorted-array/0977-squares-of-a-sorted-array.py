class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [nums[i]**2 for i in range(len(nums))]
        nums.sort()
        return nums