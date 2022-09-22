class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # @lru_cache(None)
        # def whoWin(turn, Al, Bo, arr):
        #     if not arr:
        #         if Al > Bo:
        #             return True
        #         return False
        #     if turn:
        #         left = whoWin(not turn, Al + arr[0], Bo, arr[1:])
        #         right = whoWin(not turn, Al + arr[-1], Bo, arr[:len(arr) - 1])
        #     if not turn:
        #         left = whoWin(not turn, Al, Bo + arr[0], arr[1:])
        #         right = whoWin(not turn, Al, Bo + arr[-1], arr[:len(arr) - 1])
        #     return left or right
        # return whoWin(True, 0, 0, piles)
        return True
                