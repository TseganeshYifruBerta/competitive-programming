class Solution:
    def addCapital(self, w, heap, capital_profit):
        while capital_profit and capital_profit[-1][0] <= w:
                c, p = capital_profit.pop()
                heappush(heap, -p)
                
                
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_profit = [[capital[i], profits[i]] for i in range(len(profits))]
        
        capital_profit.sort(reverse = True)
        
        heap = []
        self.addCapital(w, heap, capital_profit)
        
        while heap and k > 0:
            prof = heappop(heap)
            w -= prof
            self.addCapital(w, heap, capital_profit)
            k -= 1
            
        return w
            
        
          