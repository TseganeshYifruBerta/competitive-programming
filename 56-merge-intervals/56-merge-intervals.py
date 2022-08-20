class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans, p = [], 0
        while p < len(intervals):
            start = intervals[p][0]
            temp = intervals[p]
            while p < len(intervals) and temp[1] >= intervals[p][0]:
                temp = [start,max(temp[1], intervals[p][1])]
                p += 1
            ans.append([start, temp[1]])
        return ans
            