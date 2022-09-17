class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        word_map = {}
        for i in range(len(words)):
            word_map[words[i]] = i
            
            
        res = set()
        for i, word in enumerate(words):
            if not word:
                continue
                
                
            for j in range(len(word)):
                current = word[:j]
                target = word[j:][::-1]
                if current == current[::-1] and target != word and target in word_map:
                    res.add((word_map[target], i))
                    
            
            
            
            for j in range(len(word), -1, -1):
                current = word[j:]
                target = word[:j][::-1]
                if current == current[::-1] and target != word and target in word_map:
                    res.add((i, word_map[target]))
                    
            
            
            if word == word[::-1] and "" in word_map:
                idx = word_map[""]
                res.add((i, idx))
                res.add((idx, i))

        return list(res)