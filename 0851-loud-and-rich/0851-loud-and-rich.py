class Solution:
    
    def buildgraph(self, richer):
        graph = defaultdict(list)
        for a, b in richer:
            graph[b].append(a)
        return graph
    
    def buildindegree(self, richer):
        indegree = defaultdict(int)
        for a, b in richer:
            indegree[a] += 1
        return indegree
    
    
    def dfs(self, node, graph, quiet, dp):
        
        if dp[node] == None:
            minn = [quiet[node], node]
            
            for n in graph[node]:
                cur = self.dfs(n, graph, quiet, dp)
                if minn[0] > cur[0]:
                    minn = cur
                    
            dp[node] = minn
            
        return dp[node]
            
            
    
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = self.buildgraph(richer)
        indegree = self.buildindegree(richer)
        ans = []
        dp = [None] * len(quiet)
        
        for node in range(len(quiet)):
            self.dfs(node, graph, quiet, dp)
                
                
        for node in range(len(dp)):
            dp[node] = dp[node][1]
            
        return dp
    