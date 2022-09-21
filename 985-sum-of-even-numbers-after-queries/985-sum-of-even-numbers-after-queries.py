class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        summ = 0
        for i in nums:
            if i % 2 == 0:
                summ += i
        for val, idx in queries:
            if (nums[idx] + val ) % 2 == 0:
                if nums[idx] % 2 == 0:
                    summ += val
                else:
                    summ += nums[idx] + val
            else:
                if nums[idx] % 2 == 0:
                    summ -= nums[idx]
            nums[idx] += val
            ans.append(summ)
        return ans
            