class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        p = len(arr) - 1
        minn, res = arr[p], None
        while p >= 0:
            if arr[p] > minn:
                res = p
                break
            minn = min(minn, arr[p])
            p -= 1
        minn = -inf
        if not res and res != 0:
            return arr
        for i in range(res + 1, len(arr)):
            if minn < arr[i] < arr[res]:
                last = i
                minn = max(minn, arr[i])
        arr[res], arr[last] = arr[last], arr[res]
        return arr