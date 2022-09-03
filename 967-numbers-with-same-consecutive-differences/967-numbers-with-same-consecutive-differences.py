class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        q = deque([i for i in range(1, 10)])
        for i in range(1, n):
            newq = [] 
            for num in q:
                if (num % 10) == (num % 10 - k):
                    newq.append(num * 10 + (num % 10 - k))
                    continue
                if (num % 10 - k) >= 0:
                    newq.append(num * 10 + (num % 10 - k))
                if (num % 10 + k) <= 9:
                    newq.append(num * 10 + (num % 10 + k))
            q = newq
        return q