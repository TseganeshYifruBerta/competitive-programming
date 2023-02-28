class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxx = max(count.values())
        minn = inf
        for i in count:
            if count[i] == maxx:
                left, right = 0, len(nums) - 1

                while nums[left] != i:
                    left += 1
                while nums[right] != i:
                    right -= 1
                minn = min(right - left + 1, minn)
        return minn