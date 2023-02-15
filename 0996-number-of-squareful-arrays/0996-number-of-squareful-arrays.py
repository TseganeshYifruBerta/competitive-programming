class Solution(object):
    def numSquarefulPerms(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def isPerfectSquare(num):
            sq_root = num ** 0.5
            
            return math.ceil(sq_root) ** 2 == num or math.floor(sq_root) ** 2 == num

        edges = collections.defaultdict(set)

        
        for i1 in range(len(nums)):
            for i2 in range(len(nums)):
                if i1 != i2:
                    num1, num2 = nums[i1], nums[i2]
                    sum_of_nums = num1 + num2
                    if isPerfectSquare(sum_of_nums):
                        
                        
                        edges[num1].add((i2, num2))
                        edges[num2].add((i1, num1))
                    
        sequences = set()
        def dfs(num, visited):
            
            if len(visited) == len(nums):

                sequences.add(tuple(map(lambda x: x[1], visited)))

                
            seen = set()
            for nextNumTuple in edges[num]:
                
                if not nextNumTuple in visited and nextNumTuple[1] not in seen:
                    seen.add(nextNumTuple[1])
                    visited.append(nextNumTuple)
                    dfs(nextNumTuple[1], visited)
                    
                    visited.pop()

                    
        seen = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                dfs(nums[i], [(i, nums[i])])

        return len(sequences)