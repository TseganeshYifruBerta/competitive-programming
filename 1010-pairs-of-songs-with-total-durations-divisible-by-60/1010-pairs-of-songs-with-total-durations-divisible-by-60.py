class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dictionary = defaultdict(int)
    
        for t in time:
            dictionary[t%60] += 1
            
            
        sett =set()
        answer = 0
        for t in dictionary:
            diff = 60 - t
            if diff in dictionary and diff not in sett:
                sett.add(diff)
                sett.add(t)
                if diff != t:
                    answer += dictionary[diff] * dictionary[t]
                else:
                    
                    let = dictionary[t] - 1
                    answer += (let * (let + 1) )//2
        if 0 in dictionary:
            let = dictionary[0] - 1
            answer += (let * (let + 1) )//2
            
        return answer