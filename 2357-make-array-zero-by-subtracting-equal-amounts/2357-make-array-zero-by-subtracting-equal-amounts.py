class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        sett = set(nums)
        if 0 in sett: return len(sett) - 1
        return len(sett)