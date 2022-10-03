from sortedcontainers import SortedList
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        p = 0
        totalTime = 0
        while p < len(colors):
            temp = colors[p]
            lst = SortedList([])
            while p < len(colors) and temp == colors[p]:
                lst.add(neededTime[p])
                p += 1
            if len(lst) > 1:
                totalTime += sum(lst[:len(lst) - 1])
        return totalTime
            