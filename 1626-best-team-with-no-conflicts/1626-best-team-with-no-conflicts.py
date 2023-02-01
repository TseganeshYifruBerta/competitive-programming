class Solution:
    def maxScore(self, players, maxx, prev, memo):
        if maxx < 0:
            return 0
        
        if (maxx, prev) not in memo:
            
            if players[maxx] <= prev:
                pick = players[maxx] + self.maxScore(players, maxx - 1, players[maxx], memo)
                unpick = self.maxScore(players, maxx - 1, prev, memo)
                memo[(maxx, prev)] = max(pick, unpick)
            else:
                memo[(maxx, prev)] = self.maxScore(players, maxx - 1, prev, memo)
        return memo[(maxx, prev)]
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = []
        for i in range(len(ages)):
            players.append((ages[i], scores[i]))
            
            
        players.sort()
        scores = [x[1] for x in players]
        for i in range(len(scores)):
            scores[i] = players[i][1]
        
        
        answer = self.maxScore(scores, len(scores) - 1, inf, {})
        return answer
    
            
        