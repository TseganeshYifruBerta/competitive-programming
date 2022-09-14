class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1]
        backward = [1]
        for i in range(len(nums) - 1):
            forward.append(forward[-1] * nums[i])
        for i in range(len(nums) - 1, 0, -1):
            backward.append(backward[-1] * nums[i])
            
        backward.reverse()
        
        ans = []
        for i in range(len(backward)):
            ans.append(backward[i] * forward[i])
        return ans