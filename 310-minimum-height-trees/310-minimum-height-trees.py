class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 0: return []
        if n == 1: return [0]
        indegree = defaultdict(int)
        adj = defaultdict(list)
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
            indegree[node2] += 1
            indegree[node1] += 1
            
        q = deque([])
        
        for i in indegree:
            if indegree[i] == 1:
                q.append(i)
            
        while n > 2:
            size = len(q)
            n -= size
            while size > 0:
                cur = q.popleft()
                for i in adj[cur]:
                    indegree[i] -= 1
                    if indegree[i] == 1:
                        q.append(i)
                size -= 1
        return q