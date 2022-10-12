class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        seen = set()
        q = deque([('0000', 0)])
        seen.add('0000')
        while q:
            val, turn = q.popleft()
            if val == target:
                return turn
            
            if val in deadends:
                continue
            for i in range(4):
                for j in [1, -1]:
                    temp = val[:i] + str((int(val[i]) + j) % 10) + val[i + 1:] 
                    if temp not in seen:
                        seen.add(temp)
                        q.append((temp , turn + 1))
                        
        return -1
                        
        