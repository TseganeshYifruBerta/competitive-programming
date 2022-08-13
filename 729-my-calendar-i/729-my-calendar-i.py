class MyCalendar:
    def __init__(self):
        self.myCalander = []

    def book(self, start: int, end: int) -> bool:
        # self.myCalander.sort()
        if self.myCalander == []:
            self.myCalander.append([start,end])
            return True
        else:
            for s,e in self.myCalander:
                if not (s>= end or start >= e):
                    return False
            self.myCalander.append([start,end])
            return True