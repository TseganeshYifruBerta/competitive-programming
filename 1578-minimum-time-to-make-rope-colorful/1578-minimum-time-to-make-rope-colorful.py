from sortedcontainers import SortedList
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        p, totalTime = 0, 0
        
        while p < len(colors):
            
            temp, maxx = colors[p], 0
            while p < len(colors) and temp == colors[p]:
                maxx = max(maxx, neededTime[p])
                p += 1
                
            totalTime += maxx
            
            
        return sum(neededTime) - totalTime
            