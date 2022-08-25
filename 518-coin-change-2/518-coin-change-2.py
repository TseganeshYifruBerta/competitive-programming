class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def posCoins(idx, summ):
            if summ == 0:
                return 1
            if summ < 0:
                return 0
            count = 0
            for i in range(idx, len(coins)):
                if summ >= coins[i]:
                    count += posCoins(i, summ - coins[i])
            return count
        return posCoins(0, amount)
                
            