class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @lru_cache(None)
        def dp(remain, idx):
            if remain == 0:
                if idx == len(jobDifficulty): return 0
                return inf
            if idx == len(jobDifficulty):
                return inf
            
            minn = inf
            curmax = 0
            for i in range(idx, len(jobDifficulty)):
                curmax = max(curmax, jobDifficulty[i])
                minn = min(minn, curmax + dp(remain - 1, i + 1))
            return minn
        
        if len(jobDifficulty) < d:
            return -1
        return dp(d, 0)