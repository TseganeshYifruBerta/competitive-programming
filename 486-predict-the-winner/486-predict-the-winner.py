class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def whoWin(left, right):
            if left == right:
                return nums[right]
            start = nums[left] - whoWin(left + 1, right)
            end = nums[right] - whoWin(left, right - 1)
            return max(start, end)
        return whoWin(0, len(nums) - 1) >= 0
            
        