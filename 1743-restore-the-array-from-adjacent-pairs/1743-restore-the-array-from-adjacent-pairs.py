class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        dictionary = defaultdict(list)
        visited = set()
        for u, v in adjacentPairs:
            dictionary[u].append(v)
            dictionary[v].append(u)
            
        answer = [0 for i in range(len(adjacentPairs) + 1)]
        
        for i in dictionary:
            if len(dictionary[i]) == 1:
                answer[0] = i
                answer[1] = dictionary[i][0]
                cur = dictionary[i][0]
                visited.add(i)
                visited.add(dictionary[i][0])
                break
                
        for i in range(2, len(answer)):
            for j in dictionary[answer[i - 1]]:
                if j not in visited:
                    answer[i] = j
                    visited.add(j)
        return answer
                
                
            
        