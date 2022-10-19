class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = sqrt((x**2) + (y**2))
            heappush(heap, (distance, [x, y]))
            
        answer = []
        for i in range(k):
            min_distance, point = heappop(heap)
            answer.append(point)
        return answer