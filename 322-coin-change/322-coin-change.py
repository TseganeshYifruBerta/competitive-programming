class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def minCoin(coin):
            if coin < 0: return -1
            if coin == 0: return 0
            count = inf
            for i in range(len(coins)):
                temp = 1 + minCoin(coin - coins[i])
                if temp == 0: 
                    continue
                count = min(count, temp)
            if count == inf:
                return -1
            return count
        return minCoin(amount)