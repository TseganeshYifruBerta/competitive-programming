class Solution(object):
    def secondsToRemoveOccurrences(self, s):
        ans = 0
        while s.count("01") > 0 :
            s = s.replace("01", "10");
            ans += 1
        return ans