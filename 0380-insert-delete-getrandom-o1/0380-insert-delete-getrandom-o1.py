class RandomizedSet:

    def __init__(self):
        self.val_to_idx = {}
        self.rand_list = []

    def insert(self, val: int) -> bool:
        if val not in self.val_to_idx:
            self.rand_list.append(val)
            self.val_to_idx[val] = len(self.rand_list) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
    
        if val in self.val_to_idx:
            idx = self.val_to_idx[val]
            self.rand_list[idx], self.rand_list[-1] = self.rand_list[-1], self.rand_list[idx]
            
            self.val_to_idx[self.rand_list[idx]] = idx
            self.rand_list.pop()
            self.val_to_idx.pop(val)
            
            return True
        return False
        

    def getRandom(self) -> int:
        rand_idx = random.randint(0, len(self.rand_list) - 1)
        rand_val = self.rand_list[rand_idx]
        return rand_val


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()