class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        maxx = 0
        for i in nums:
            count = 1
            if i - 1 not in sett:
                cur = i + 1
                while cur in sett:
                    count += 1
                    cur += 1
                maxx = max(maxx, count)
        return maxx