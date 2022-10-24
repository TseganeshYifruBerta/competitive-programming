class Solution:
    
    def maxLength(self, arr: List[str]) -> int:
        self.ans = 0
        def subsequence(arr , index , n , temp ):
            if index >= n:
                s = ''.join(temp)
                if len(set(s)) == len(s):
                    self.ans = max(self.ans , len(s))
            else:
                #pick
                temp.append(arr[index])
                subsequence(arr , index + 1 , n , temp )
                
                #no-pick
                temp.pop()
                subsequence(arr , index + 1 , n , temp)
                

        subsequence(arr , 0 , len(arr) , [])
        return self.ans