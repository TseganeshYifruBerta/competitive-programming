class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = Counter(nums)
        
        for i in count:
            freq[count[i]].append(i)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
            if k == len(res):
                return res
        