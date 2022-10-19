class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = Counter(words)
        heap = []
        
        for char in frequency:
            heappush(heap, (-frequency[char], char))
            
        answer = []
        for i in range(k):
            freq, char = heappop(heap)
            answer.append(char)
            
        return answer