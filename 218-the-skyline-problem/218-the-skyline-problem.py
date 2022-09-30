class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        buildings.sort(key = lambda k: (k[0], -k[2]))
        buildings.append([float('inf'), float('inf'), 0])
        height_mxheap = []
        skyline = []

        for left, right, height in buildings:
            
            while height_mxheap and height_mxheap[0][1] <= left:

                _, last_right = heapq.heappop(height_mxheap)

                if last_right == left:
                    continue

                    
                while height_mxheap and height_mxheap[0][1] <= last_right:
                    heapq.heappop(height_mxheap)

                if height_mxheap: 
                    if skyline[-1][1] != -height_mxheap[0][0]:
                        skyline.append([last_right, -height_mxheap[0][0]])
                else:
                    skyline.append([last_right, 0])

            heapq.heappush(height_mxheap, (-height, right))

            max_height = -height_mxheap[0][0]
            
            if not skyline or skyline[-1][1] != max_height:
                skyline.append([left, max_height])

        return skyline