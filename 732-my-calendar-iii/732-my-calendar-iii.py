from sortedcontainers import SortedList
class MyCalendarThree:

    def __init__(self):
        self.A = SortedList()

    def book(self, start: int, end: int) -> int:
        self.A.add((start,1))
        self.A.add((end,-1))
        x=ans = 0
        for _,a in self.A:
            x += a
            ans = max(ans,x)
        return ans