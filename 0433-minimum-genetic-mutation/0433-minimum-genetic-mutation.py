class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        def checkNeighbor(a,b):
            return sum([1 for i in range(len(a)) if a[i]!=b[i]]) == 1
        
        q = deque([[start,0]])
        
        visited = {start}
        while q:
            cur, mutations = q.popleft()
            
            if cur == end:
                return mutations
            
            for nei in bank:
                
                if checkNeighbor(cur,nei) and nei not in visited:
                    visited.add(nei)
                    q.append([nei,mutations+1])
        return -1