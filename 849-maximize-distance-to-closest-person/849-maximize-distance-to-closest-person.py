class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        maxx = 0
        countl = 0
        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 1:
                break
            countl += 1
        countr = 0
        for i in range(len(seats)):
            if seats[i] == 1:
                break
            countr += 1
            
        
        p1, p2 = i, i + 1
        
        while p2 < len(seats):
            count = 0
            while p2 < len(seats) and seats[p2] == 0:
                count += 1
                p2 += 1
            maxx = max(maxx, count)
            p1 = p2
            p2 += 1
        return max(ceil(maxx/2), countl, countr)