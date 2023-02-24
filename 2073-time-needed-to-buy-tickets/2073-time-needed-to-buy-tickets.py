class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = tickets[k]
        saved = 0
        answer = 0
        
        for i in range(len(tickets)):
            answer += total
            saved += max(total - tickets[i], 0)
            if i == k:
                total -= 1
                
        answer -= saved
        return answer