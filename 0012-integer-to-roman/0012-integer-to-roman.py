class Solution:
    def intToRoman(self, num: int) -> str:
        nums = {
            0: ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
            2: ['' ,'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
            1 : ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
            3: ["", "M", "MM", "MMM"]
        }
        num = str(num)
        ans = []
        p, p1 = len(num) - 1, 0
        while p >= 0:
            ans.append(nums[p1][int(num[p])])
            p -= 1
            p1 += 1
        ans.reverse()
        return "".join(ans)
        