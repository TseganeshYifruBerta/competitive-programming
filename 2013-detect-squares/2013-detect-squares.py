class DetectSquares:

    def __init__(self):
        self.pointes = Counter()
        
        

    def add(self, point: List[int]) -> None:
        self.pointes[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        answer = 0
        
        x, y = point
       
        for p in self.pointes:
            xi, yi = p
            absy = abs(y - yi)
            absx = abs(x - xi)
            
            if absx == absy and absx:
                answer += (self.pointes[p] * self.pointes[(xi, y)] * self.pointes[(x, yi)])
        return answer


# # Your DetectSquares object will be instantiated and called as such:
# # obj = DetectSquares()
# # obj.add(point)
# # param_2 = obj.count(point)


# from collections import Counter
# class DetectSquares:

#     def __init__(self):
#         self.counter = Counter()
        

#     def add(self, point: List[int]) -> None:
#         self.counter[tuple(point)] += 1
        

#     def count(self, point: List[int]) -> int:
#         res = 0
#         x, y = point
#         for x0, y0 in self.counter.keys():
#             if abs(x-x0) == abs(y-y0) and abs(x-x0):
#                 res += self.counter[(x0,y0)]*self.counter[(x0,y)]*self.counter[(x,y0)]
#         return res
