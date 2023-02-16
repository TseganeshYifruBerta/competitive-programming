class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = nums[0]
        max_so_far = nums[0]
        for i in range(1, len(nums)):
            cur = max(cur + nums[i], nums[i])
            max_so_far = max(cur, max_so_far)
        return max_so_far