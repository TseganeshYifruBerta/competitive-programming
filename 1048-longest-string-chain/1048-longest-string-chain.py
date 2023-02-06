class Solution:
    def checkSubsequence(self, dictionary, target, chain):
        for word in dictionary[len(target) + 1]:
            
            pointer = 0
            mismatch = 0
            for char in word:
                
                if pointer < len(target) and char == target[pointer]:
                    
                    pointer += 1
                    
                else:
                    
                    mismatch += 1
                    
                if mismatch > 1:
                    break
                    
                    
            if pointer == len(target) and mismatch == 1:
                
                chain[target].append(word)
                
                
                
    def dfs(self, wordchain, chain, memo):
        if wordchain in memo:
            return memo[wordchain]
        answer = 0
        for nextchain in chain[wordchain]:
            if nextchain in chain:
                cur = 1 + self.dfs(nextchain, chain, memo)
            else:
                cur = 1
            answer = max(cur, answer)
        
        memo[wordchain] = answer
        return answer
            
        
        
            
        
    
    def longestStrChain(self, words: List[str]) -> int:
        dictionary = defaultdict(list)
        
        for word in words:
            dictionary[len(word)].append(word)
            
            
        chain = defaultdict(list)
        for word in words:
            self.checkSubsequence(dictionary, word, chain)
            
            
            
        answer = 1
        memo = defaultdict(int)
        for word in chain:
            cur = self.dfs(word, chain, memo)
            
            answer = max(answer, cur + 1)
            
            
        return answer
    
            
            
        
            
        
        