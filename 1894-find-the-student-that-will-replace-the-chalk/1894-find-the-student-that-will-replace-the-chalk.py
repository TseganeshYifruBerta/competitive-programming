class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        summ = sum(chalk)
        k = k % summ
        for i in range(len(chalk)):
            if k - chalk[i] < 0:
                return i
            k -= chalk[i]
            
        