class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree, incoming = [0 for i in range(numCourses)], defaultdict(list)
        for pre in prerequisites:
            a, b = pre
            incoming[b].append(a)
            indegree[a] += 1    
        q = deque()
        ans = []
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        while q:
            course = q.popleft()
            ans.append(course)
            for c in incoming[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)
                    
        if len(ans) == numCourses:
            return ans
        return []
                
        
        
            