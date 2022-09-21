class Solution:
    def dfs_route_count(self, cur, graph, last_node, memo):
        
        if cur == last_node:
            return 1
        
        if cur in memo:  
            return memo[cur]
        
        count = 0
        for nbr,_ in graph[cur]:
            
            if self.dist_to_last[cur] > self.dist_to_last[nbr]:
                count = count%(10**9 + 7) + self.dfs_route_count(nbr, graph, last_node, memo)%(10**9+7)
                
        memo[cur] = count
        return count
         
    def make_dist_to_last(self, last_node, graph):
        dist_to_last = {} 
        visited = set() 
        minheap = [(0, last_node)]
        
        while len(minheap) > 0:
            cost, cur = heappop(minheap)
            
            if cur in visited:
                continue
                
            visited.add(cur)    
            dist_to_last[cur] = cost
            
            for nbr, weight in graph[cur]:
                if nbr in visited:
                    continue
                heappush(minheap, (weight + cost, nbr) )
               
        return dist_to_last    
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        # make graph
        graph = {i:[] for i in range(1, n+1)}
        for start, end, weight in edges:
            graph[start].append( (end, weight) )
            graph[end].append( (start, weight) )
        
        self.dist_to_last = self.make_dist_to_last(n, graph)        
        memo = dict()
        return self.dfs_route_count(1, graph, n, memo)