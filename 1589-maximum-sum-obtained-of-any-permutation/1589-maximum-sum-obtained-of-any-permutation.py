class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0 for i in range(len(nums) + 1)]
        
        for start, end in requests:
            prefix[start] += 1
            prefix[end + 1] -= 1
            
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]
            
            
        sortedd = [(prefix[i], i) for i in range(len(nums))]
        sortedd.sort(reverse = True)
        
        answer = [0 for i in range(len(prefix))]
        nums.sort(reverse = True)
        
        for i in range(len(nums)):
            answer[sortedd[i][1]] = nums[i]
            
        result = 0
        for i in range(len(answer)):
            result += answer[i] * prefix[i]
            
        return (result) % (1000000007)
        