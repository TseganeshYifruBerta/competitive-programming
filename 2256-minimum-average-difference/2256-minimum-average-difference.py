class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        backward = [nums[-1]]
        forward = [nums[0]]
        ans = [inf, -1]
        for i in range(1, len(nums)):
            forward.append(forward[-1] + nums[i])
            backward.append(backward[-1] + nums[-i - 1])
        backward.reverse()
        
        for i in range(len(nums) - 1):
            left = forward[i] // (i + 1)
            right = backward[i + 1] // (len(nums) - i  - 1)
            res = abs(left - right)
            if res < ans[0]:
                ans = [res, i]
                
        if abs(forward[-1] / len(nums)) < ans[0]:
            ans = [forward[-1] / len(nums), len(nums) - 1]
        return ans[1]