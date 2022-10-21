class Solution:
    def buildindegree(self, edges):
        indegree = defaultdict(int)
        for a, b in edges:
            indegree[a] += 1
            indegree[b] += 1
        return indegree
    
    def buildgraph(self, edges):
        outgoing = defaultdict(list)
        for a, b in edges:
            outgoing[a].append(b)
            outgoing[b].append(a)
        return outgoing
    
    def detectcycle(self, graph, visited, indegree):
        q = deque()
        for node in graph:
            if indegree[node] == 1:
                indegree[node] -= 1
                q.append(node)
                
        while q:
            node = q.popleft()
            if node in visited:
                continue
            visited.add(node)
            for n in graph[node]:
                indegree[n] -= 1
                if indegree[n] == 1:
                    q.append(n)
        return visited
    
        
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = self.buildgraph(edges)
        indegree = self.buildindegree(edges)
        visited = self.detectcycle(graph, set(), indegree)
        
        for i in reversed(range(len(edges))):
            a, b = edges[i]
            if a not in visited and b not in visited:
                return [a, b]
        
        