class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        r = 0 
        l = 0 
        n = len(nums)
        recentMin = -1 
        recentMax = -1 
        while r < n:
            while r<n: 
                num = nums[r]
                if not minK<=num<=maxK: 
                    break

                if num == minK:
                    recentMin = r
                if num == maxK:
                    recentMax = r
                r += 1
                if recentMin != -1 and recentMax != -1:
                    ans += (min(recentMin,recentMax)-l)+1 
            r+=1
            l = r
            recentMin = -1
            recentMax = -1
        return ans
