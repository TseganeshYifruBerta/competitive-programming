class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = defaultdict(int)
        d[0] = -1
        if nums[0] % k not in d:
            d[nums[0] % k] = 0
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            if nums[i] % k in d and i - d[nums[i] % k] >= 2:
                return True
            elif nums[i] % k not in d:
                d[nums[i] % k] = i
        return False
        