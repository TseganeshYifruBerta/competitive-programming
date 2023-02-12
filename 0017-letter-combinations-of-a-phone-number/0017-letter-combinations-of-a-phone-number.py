class Solution:
    def backtracking(self, digits, dictionary, index, answer):
        if index >= len(digits):
            return answer

        temp_ans = []
        for char in dictionary[digits[index]]:
            for word in answer:
                temp_ans.append(word + char)

        return self.backtracking(digits, dictionary, index + 1, temp_ans)
            

    def letterCombinations(self, digits: str) -> List[str]:
        dictionary = {
                        '2': ['a', 'b', 'c'],
                        '3': ['d', 'e', 'f'],
                        '4': ['g', 'h', 'i'],
                        '5': ['j', 'k', 'l'], 
                        '6': ['m', 'n', 'o'], 
                        '7': ['p', 'q', 'r', 's'],
                        '8': ['t', 'u', 'v'],
                        '9': ['w', 'x', 'y', 'z']
        }
        if len(digits) == 0: return []
        combinations = self.backtracking(digits, dictionary, 1, dictionary[digits[0]])
        return combinations
        