class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lst = []
        p = 0
        while p < len(words):
            count = 0
            k = maxWidth
            while p < len(words) and k - len(words[p]) > count - 1:
                k -= len(words[p])
                count += 1
                p += 1
            lst.append((count, k))
        count = 0
        res = []
        for freq, remain in lst:
            ans = words[count]
            if freq != 1:
                temp = ' ' * (remain // (freq - 1))
            else:
                temp = ' ' * remain
                
            for i in range(count + 1, count + freq):
                ans += temp
                if i - count - 1 < (remain % (freq - 1)):
                    ans += ' '
                ans += words[i]
            count += freq
            if len(ans) < maxWidth:
                ans += temp
            res.append(ans)
        temp = lst[-1]
        ans = ''
        for i in range(len(words) - temp[0], len(words) - 1):
            ans += words[i] + ' '
        ans += words[-1]
        t = ' ' * (maxWidth - len(ans))
        
        ans += t
        res[-1] = ans
        return res
            
            