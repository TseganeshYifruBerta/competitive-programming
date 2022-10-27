class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        connections = [[False for i in range(numCourses)] for j in range(numCourses)]
        
        for a, b in prerequisites:
            connections[a][b] = True
        
        for intermidiate in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if connections[i][intermidiate] and connections[intermidiate][j]:
                        connections[i][j] = True
        
        answer = []
        for a, b in queries:
            answer.append(connections[a][b])
        return answer