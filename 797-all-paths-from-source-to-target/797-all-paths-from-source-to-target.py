class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.ans = []
        
        def backtrack(node, lst):
            if node == len(graph) - 1:
                self.ans.append(lst + [node])
            
            for n in adj[node]:
                backtrack(n, lst + [node])
                
        adj = defaultdict(list)
        for i in range(len(graph)):
            for j in graph[i]:
                adj[i].append(j)
        backtrack(0, [])  
        return self.ans
        
        
        