class TimeMap:
    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict:
            self.dict[key].append((timestamp, value))
        else:
            self.dict[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
		# Get value from binary search
        if key not in self.dict or timestamp < self.dict[key][0][0]:
            return ""
        elif timestamp > self.dict[key][len(self.dict[key]) - 1 ][0]:
            return self.dict[key][len(self.dict[key]) - 1 ][1]
        else:
            result = self.bs(key, timestamp)
            return result
    
    def bs(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.dict[key]) - 1 
        while left <= right:
            mid = (left + right) // 2
            if self.dict[key][mid][0] == timestamp:
                return self.dict[key][mid][1]
            if self.dict[key][mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        return self.dict[key][left - 1][1]