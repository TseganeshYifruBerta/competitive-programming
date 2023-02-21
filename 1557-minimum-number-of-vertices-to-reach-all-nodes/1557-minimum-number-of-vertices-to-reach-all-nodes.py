class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        answer = []
        indegree = defaultdict(int)
        for a, b in edges:
            indegree[b] += 1
            
        for i in range(n):
            if i not in indegree:
                answer.append(i)
                
        return answer