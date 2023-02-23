class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        def addCapital(w, heap, capital_profit):
            while capital_profit and capital_profit[-1][0] <= w:
                c, p = capital_profit.pop()
                heappush(heap, -p)
                
            
            
            
        capital_profit = []
        for i in range(len(profits)):
            capital_profit.append([capital[i], profits[i]])
        capital_profit.sort(reverse = True)
        
        
        
        heap = []
        addCapital(w, heap, capital_profit)
        while heap and k > 0:
            prof = heappop(heap)
            w -= prof
            
            addCapital(w, heap, capital_profit)
            k -= 1
            
        return w
            
        
          