class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def shortest(house):
            left, right = 0, len(heaters) - 1
            short = inf
            while right >= left:
                mid = (left + right) // 2
                short = min(short, abs(heaters[mid] - house))
                if house > heaters[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return short
        
        heaters.sort()
        rad = 0
        for i in houses:
            rad = max(rad, shortest(i))
        return rad