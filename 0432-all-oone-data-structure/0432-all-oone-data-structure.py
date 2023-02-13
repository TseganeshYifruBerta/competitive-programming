class AllOne:
    def __init__(self):
        self.count = defaultdict(int) 
        self.record = defaultdict(set) 
        

    def inc(self, key: str) -> None:
        
        self.count[key] += 1    
        self.record[self.count[key]].add(key)
        
        if self.count[key] > 1: 
            self.record[self.count[key] - 1].remove(key)
            if not self.record[self.count[key] - 1]: 
                del self.record[self.count[key] - 1]
                
    def dec(self, key: str) -> None:
        
        self.count[key] = self.count[key]-1
        if self.count[key]:
            self.record[self.count[key]].add(key)
        self.record[self.count[key]+1].remove(key)

        if not self.record[self.count[key]+1]:
            del self.record[self.count[key]+1]

        return

    def getMaxKey(self) -> str:
        
        maxx = max(self.record.keys()) if self.record.keys() else 0
        return next(iter(self.record[maxx])) if maxx else ""

    def getMinKey(self) -> str:
        
        minn = min(self.record.keys()) if self.record.keys() else 0
        return next(iter(self.record[minn])) if minn else ""