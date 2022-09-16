class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)
        indegree = defaultdict(list)
        
        for n, m in edges:
            indegree[n].append(m)
            indegree[m].append(n)
        
        q = deque([0])
        count = 0
        restricted.add(0)
        while q:
            cur = q.popleft()
            count += 1
            for i in indegree[cur]:
                if i not in restricted:
                    q.append(i)
                restricted.add(i)
        return count