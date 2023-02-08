class Solution:
    def buildGraph(self, routes):
        graph = defaultdict(set) 
        
        for route_id, stops in enumerate(routes):
            for stop in stops:
                graph[stop].add(route_id)  
                
        return graph
    
    
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = self.buildGraph(routes)
        
        q = deque([(source, 0)])

        visitedDest = set([source])
        visitedRt = set()
        
        while q:
            stop, num_changes = q.popleft()
            if stop == target:
                return num_changes

            for route_id in graph[stop]:
                if route_id not in visitedRt:
                    visitedRt.add(route_id)

                    for stop in routes[route_id]:
                        if stop not in visitedDest:
                            visitedDest.add(stop)
                            q.append((stop, num_changes + 1))
        
        return -1