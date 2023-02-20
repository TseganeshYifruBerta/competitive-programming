class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
#         maxx = -1
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[j] > nums[i]:
#                     maxx = max(maxx, nums[j] - nums[i])
                    
#         return maxx
        
        minn = inf
        ans = -1
        for i in range(len(nums)):
            minn = min(minn, nums[i])
            
            if nums[i] > minn:
                ans = max(ans, nums[i] - minn)
            
            
        return ans
            