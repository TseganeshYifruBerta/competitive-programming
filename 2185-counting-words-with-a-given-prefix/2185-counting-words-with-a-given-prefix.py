class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        answer = 0
        for word in words:
            if word[:len(pref)] == pref:
                answer += 1
        return answer
      
      
      
      
      
      
      
class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.count = 0
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        root = Trie()
        def insert(root, word):
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = Trie()
                curr.count += 1
                curr = curr.children[c]
            curr.count += 1
            curr.isEnd = True
        def startswith(root, pre):
            curr = root
            for c in pre:
                if c not in curr.children:
                    return 0
                curr = curr.children[c]
            return curr.count
        for word in words:
            insert(root, word)
        return startswith(root, pref)
        
