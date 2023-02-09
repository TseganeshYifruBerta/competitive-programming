class Solution:
    def maximumSwap(self, num: int) -> int:
        ans=[]  
        num=str(num)
        lst=list(map(str,num))

        for x in range(len(lst)):
            for y in range(x,len(lst)):
                lst[x],lst[y]=lst[y],lst[x]
                res=''.join(lst)
                ans.append(int(res))
                lst=list(map(str,num))

        if len(ans)==0:
            return int(num)
        return max(ans)