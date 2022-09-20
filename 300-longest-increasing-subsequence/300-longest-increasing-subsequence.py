class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        temp = []
        for n in nums:
            i = bisect.bisect_left(temp, n)
            if i != len(temp):
                temp[i] = n
            else:
                temp.append(n)
        return len(temp)