class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # frequency table to store the frequency of the remainder
        dictionary = defaultdict(int)
        
        dictionary[0] = 1
        
        res = prefixSum = 0
        for n in nums:
            
            prefixSum += n
            
            remainder = prefixSum % k
            
            res += dictionary[remainder]
            
            dictionary[remainder] += 1
        return res