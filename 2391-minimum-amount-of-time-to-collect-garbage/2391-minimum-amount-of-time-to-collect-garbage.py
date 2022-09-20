class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        for i in range(1, len(travel)):
            travel[i] += travel[i - 1]
        
        summ = defaultdict(int)
        last = {}
        for i in range(len(garbage)):
            for j in garbage[i]:
                summ[j] += 1
                last[j] = i
        res = 0
        for i in last:
            temp = last[i] - 1
            if temp >= 0:
                res += travel[temp] + summ[i]
            else:
                res += summ[i]
        return res
            
        
                