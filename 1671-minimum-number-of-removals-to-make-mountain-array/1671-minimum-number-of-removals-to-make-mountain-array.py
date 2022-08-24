class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        def helper(arr):
            dp = [1] * len(nums)
            for i in range(1, len(arr)):
                for j in range(i):
                    if arr[i] > arr[j]:
                        dp[i] = max(dp[i], 1 + dp[j])
            return dp.copy()
        fDp = helper(nums)
        nums.reverse()
        bDp = helper(nums)
        bDp.reverse()
        minn = inf
        for i in range(1, len(nums) - 1):
            temp = len(nums) - (fDp[i] + bDp[i] - 1)
            if fDp[i] != 1 and bDp[i] != 1:
                minn = min(minn, temp)
        return minn
            
        