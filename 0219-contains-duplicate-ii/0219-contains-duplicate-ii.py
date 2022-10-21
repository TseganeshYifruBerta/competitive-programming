class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter = {}
        
        for num in range(len(nums)):
            if nums[num] in counter:
                if num - counter[nums[num]] <= k:
                    return True
            counter[nums[num]] = num
        