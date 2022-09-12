class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        p1, p2 = 0, len(tokens) - 1
        score, max_s = 0, 0
        while p2 >= p1:
            if tokens[p1] <= power:
                power -= tokens[p1]
                score += 1
                p1 += 1
            elif tokens[p2] > power and score > 0:
                power += tokens[p2]
                score -= 1
                p2 -= 1
            else:
                return max_s
            max_s = max(max_s, score)
        return max_s
#         two pointers
#         if power < token[p1] : 
#         if power >= token[p2]
#         
            