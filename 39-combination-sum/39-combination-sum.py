class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        def backtrack(idx, path, summ):
            if summ > target:
                return 
            if summ == target:
                self.ans.append(path)
                return
            for i in range(idx, len(candidates)):
                backtrack(i, path + [candidates[i]], summ + candidates[i])
                
        backtrack(0, [], 0)
        return self.ans