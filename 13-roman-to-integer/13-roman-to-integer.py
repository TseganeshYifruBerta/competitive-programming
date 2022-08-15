class Solution:
    def romanToInt(self, s: str) -> int:
        lst = []
        p = 0
        summ = 0
        while p < len(s) :
            temp = s[p]
            st = 0
            while p < len(s) and s[p] == temp :
                if temp == 'I' :
                    st += 1
                elif temp == 'V' :
                    st += 5
                elif temp == 'X' :
                    st += 10
                elif temp == 'L' :
                    st += 50
                elif temp == 'C' :
                    st += 100
                elif temp == 'D' :
                    st += 500
                else :
                    st += 1000
                p += 1
            lst.append(st)
        for i in range(len(lst)) :
            if i - 1 >= 0 :
                if lst[i] == 5 and lst[i - 1] == 1:
                    summ += 5 - 2
                elif lst[i] == 5 :
                    summ += lst[i]
                elif lst[i] == 10 and lst[i - 1] == 1 :
                    summ += 10 - 2
                elif lst[i] == 10 :
                    summ += lst[i]
                elif lst[i] == 50 and lst[i - 1] == 10 :
                    summ += 50 - 20
                elif lst[i] == 50 :
                    summ += lst[i]
                elif lst[i] == 100 and lst[i - 1] == 10 :
                    summ += 100 - 20
                elif lst[i] == 100 :
                    summ += lst[i]
                elif lst[i] == 500 and lst[i - 1] == 100 :
                    summ += 500 - 200
                elif lst[i] == 500 :
                    summ += lst[i]
                elif lst[i] == 1000 and lst[i - 1] == 100 :
                     summ += 1000 - 200
                elif lst[i] == 1000 :
                    summ += lst[i]
                else :
                    summ += lst[i]
            else :
                summ += lst[i]
        return summ
                