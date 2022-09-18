class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        def twoP(target):
            left = 0
            right = target - 1
            ans = 0
            while right > left:
                if nums[left] + nums[right] > nums[target]:
                    ans += right - left
                    right -= 1
                else:
                    left += 1
            return ans
        count = 0
        nums.sort()
        
        for i in range(2, len(nums)):
            count += twoP(i)
            
        return count
                        