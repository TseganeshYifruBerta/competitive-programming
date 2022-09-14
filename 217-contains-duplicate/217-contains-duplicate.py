class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(Counter(nums)) != len(nums)