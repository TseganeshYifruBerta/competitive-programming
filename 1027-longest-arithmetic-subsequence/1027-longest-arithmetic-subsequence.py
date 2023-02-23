class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dic = [{} for _ in range(len(A))]
        for i in range(1,len(A)):
            for j in range(i):
                diff = A[i]-A[j]
                if diff not in dic[j]:
                    dic[i][diff] = 2
                else:
                    dic[i][diff] = 1+ dic[j][diff]
        ans = []
        for i in dic:
            ans += list(i.values())
        return max(ans)