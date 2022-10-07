class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def backtrack(purm):
            if len(purm) == len(nums):
                self.ans.append(purm)
                return
            
            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    backtrack(purm + [nums[i]])
                    visited.remove(i)
        visited = set()
        backtrack([])
        return self.ans