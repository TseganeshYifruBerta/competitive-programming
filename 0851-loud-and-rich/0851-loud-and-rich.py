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
        if node in dp:
            return dp[node]
        minn = [quiet[node], node]
        for n in graph[node]:
            cur = self.dfs(n, graph, quiet, dp)
            if minn[0] > cur[0]:
                minn = cur
        dp[node] = minn
        return minn
            
            
    
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = self.buildgraph(richer)
        indegree = self.buildindegree(richer)
        ans = []
        dp = {}
        
        for node in range(len(quiet)):
            self.dfs(node, graph, quiet, dp)
                
                
        for node in dp:
            ans.append((node, dp[node][1]))
        
        ans.sort()
        final = []
        for idx, node in ans:
            final.append(node)
        
        return final
    