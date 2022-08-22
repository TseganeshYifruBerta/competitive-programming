class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        enclosers = [[-1,-1] for _ in range(len(s))]
        lgth = len(s)
        left =  - 1
        right =  -1 
        presum = defaultdict(int)
        sm = 0
        for n in range(lgth):
            if s[n] == "|":
                left = n
                presum[n] = sm
            else:
                sm += 1
                
            if s[-(n+1)] == "|":
                right = lgth - (n+1)
                
            enclosers[n][0] = left
            enclosers[-(n+1)][1] = right

        ans = []
        for query in queries:
            l = enclosers[query[0]][1]
            r = enclosers[query[1]][0]
            if r == -1: r = l
            if l == -1: l = r
            
            if l > r:
                ans.append(0)
            else: ans.append(presum[r] - presum[l])
            
        return ans
            
        
            