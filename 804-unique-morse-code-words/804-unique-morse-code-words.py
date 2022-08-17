class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        sett = set()
        d = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            temp = ""
            for char in word:
                temp += d[ord(char) - 97]
            sett.add(temp)
        return len(sett)