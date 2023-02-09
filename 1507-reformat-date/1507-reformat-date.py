from datetime import datetime
class Solution:
    def reformatDate(self, date: str) -> str:
        date = date.split()
        date[0] = date[0][:len(date[0]) - 2]
        date = ' '.join(date)
        
        answer = str(datetime.strptime(date, "%d %b %Y"))
        return answer[:len(answer) - 9]