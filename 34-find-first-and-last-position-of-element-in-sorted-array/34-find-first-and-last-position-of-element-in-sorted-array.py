class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        ans = [-1, -1]
        while right >= left:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                first, last = mid, mid
                while first >= 0 and nums[first] == target:
                    first -= 1
                while last < len(nums) and nums[last] == target:
                    last += 1
                return [first + 1, last - 1]
        return ans