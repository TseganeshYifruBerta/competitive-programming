class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x, y, xx, yy = rec2
        
        
        if x1 >= xx or x2 <= x or y2 <= y or y1 >= yy:
            return False
        else:
            return True
      
        