class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        p1, p2, p3 = len(nums) - 3, len(nums) - 2, len(nums) - 1
        
        while p1 >= 0:
            summ = nums[p1] + nums[p2] + nums[p3]
            if 2 * nums[p1] < summ and 2 * nums[p2] < summ and 2 * nums[p3] < summ:
                return summ
            p1 -= 1
            p2 -= 1
            p3 -= 1
        return 0