class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        p1, p2 = 0, 0
        summ = nums[0]
        ans = inf
        while p2 < len(nums):
            if summ < target:
                p2 += 1
                if p2 < len(nums):
                    summ += nums[p2]
            else:
                ans = min(ans, p2 - p1 + 1)
                summ -= nums[p1]
                p1 += 1
        if ans == inf:
            return 0
        return ans