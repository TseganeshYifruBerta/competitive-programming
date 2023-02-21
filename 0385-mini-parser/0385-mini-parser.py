class Solution:
    def parseNumber(self, s, idx, isNegative=False):
        num = 0
        while idx < len(s) and s[idx].isdigit():
            num = num*10 + int(s[idx])
            idx += 1
        if isNegative:
            num = -num
        return NestedInteger(num), idx
    
    def parseList(self, s, idx):
        obj = NestedInteger()
        while idx < len(s) and s[idx] != ']':
            if s[idx].isdigit():
                data, idx = self.parseNumber(s, idx)
                obj.add(data)
            elif s[idx] == '-':
                data, idx = self.parseNumber(s, idx+1, True)
                obj.add(data)
            elif s[idx] == '[':
                data, idx = self.parseList(s, idx+1)
                obj.add(data)
            else:
                idx += 1

        return obj, idx+1
    
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            if s[0] == '-':
                nestedInteger, _ = self.parseNumber(s, 1, True)
            else:
                nestedInteger, _ = self.parseNumber(s, 0)
        else:
            nestedInteger, _ = self.parseList(s, 1)        

        return nestedInteger