class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        sender_to_message = defaultdict(int)
        for msg in range(len(messages)):
            sender_to_message[senders[msg]] += len(messages[msg].split())
            
        
        heap = []
        for sender in sender_to_message:
            heap.append((sender_to_message[sender], sender))
            
        heap.sort()
        
        return heap[-1][-1]