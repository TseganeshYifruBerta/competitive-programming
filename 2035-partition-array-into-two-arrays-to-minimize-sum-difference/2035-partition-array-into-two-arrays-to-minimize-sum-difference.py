class Solution:
    def minimumDifference(self, nums):
        def subset_sums(ans):
            d = defaultdict(set)

            for i in range(1,len(ans)):
                d[i] = sorted(set([sum(j) for j in combinations(ans,i)]))
            return d

        n = len(nums)

        total, l, r = sum(nums), nums[:n//2], nums[n//2:]
        d1, d2, min_diff = subset_sums(l), subset_sums(r), abs(sum(l)-sum(r))

        for k in d1:
            left, right = d1[k], d2[n//2-k]
            for x in left:
                i = bisect.bisect_left(right,total//2-x)

                if i<len(right):
                    min_diff = min(min_diff,abs((right[i]+x)*2-total))
                if i>0:
                    min_diff = min(min_diff,abs((right[i-1]+x)*2-total))

        return min_diff
