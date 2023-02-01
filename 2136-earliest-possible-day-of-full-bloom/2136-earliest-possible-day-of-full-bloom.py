class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        pots = []
        for i in range(len(plantTime)):
            pots.append((growTime[i], plantTime[i]))
        pots.sort(reverse = True)


        total_day = 0
        answer = 0

        for i in range(len(pots)):

            total_day += pots[i][1]

            answer = max(total_day + pots[i][0], answer)

        return answer
