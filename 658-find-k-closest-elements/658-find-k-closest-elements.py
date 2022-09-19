class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def b_search(left, right):
            minn = 0
            while right >= left:
                mid = (left + right) // 2
                if abs(arr[mid] - x) < abs(arr[minn] - x):
                    minn = mid
                if arr[mid] <= x:
                    left = mid + 1
                else:
                    right = mid - 1
            return minn
        ans = []
        mid = b_search(0, len(arr) - 1)
        
        
        left = 0 if mid - k < 0 else mid - k
        right = len(arr) if mid + k > len(arr) else mid + k
        
        for i in range(left, right):
            ans.append((abs(arr[i] - x), i))
        ans.sort()
        res = []
        for i in range(k):
            res.append(arr[ans[i][1]])
        res.sort()
        return res