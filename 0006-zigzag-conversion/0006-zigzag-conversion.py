class Solution:
    def zigzag(self, row, idx, string, hashmap, numRows, sign):
        if idx >= len(string):
            return hashmap
        
        hashmap[row].append(string[idx])
        if row == 1 or row == numRows:
            sign *= -1
        return self.zigzag(row + sign, idx + 1, string, hashmap, numRows, sign)
        
        
    def convert(self, s: str, numRows: int) -> str:
        dictionary = defaultdict(list)
        hashmap = self.zigzag(1, 0, s, dictionary, numRows, -1)
        answer = []
        for i in hashmap:
            answer += hashmap[i]
        return ''.join(answer)