class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        img1_map = []
        img2_map = []
        
        for x in range(len(img1)):
            for y in range(len(img1[0])):
                if img1[x][y] == 1:
                    img1_map.append((x, y))
        
        for x in range(len(img2)):
            for y in range(len(img2[0])):
                if img2[x][y] == 1:
                    img2_map.append((x, y))
        
        hmap = collections.defaultdict(int)
        
        for x1, y1 in img1_map:
            for x2, y2 in img2_map:
                hmap[(x1 - x2, y1 - y2)] += 1
        if len(hmap.values()) != 0:
            return max(hmap.values())
        return 0