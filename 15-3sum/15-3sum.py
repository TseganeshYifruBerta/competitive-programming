class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            left = i + 1
            right = len(nums) - 1
            while right > left:
                summ = nums[right] + nums[left] + nums[i]
                if summ  > 0:
                    right -= 1
                elif summ < 0:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and  nums[left] == nums[left - 1]:
                        left += 1
        return ans
                
                    