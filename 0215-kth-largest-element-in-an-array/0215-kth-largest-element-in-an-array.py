class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)

        for i in range(k):
            kth_maxx = heapq.heappop(nums)
        return -kth_maxx
        