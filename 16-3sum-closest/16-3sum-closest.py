class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        diff = 10**10
        ans = 0
        for i in range(n):
            newTarget = target - nums[i]
            j = i+1
            k = n-1
            while(j < k):
                if nums[j] + nums[k] == newTarget:
                    return target
                if diff > abs(nums[i]+nums[j]+nums[k]-target):
                    diff = abs(nums[i]+nums[j]+nums[k]-target)
                    ans = nums[i]+nums[j]+nums[k]
                if nums[j] + nums[k] > newTarget:
                    k -= 1
                else:
                    j += 1
        return ans