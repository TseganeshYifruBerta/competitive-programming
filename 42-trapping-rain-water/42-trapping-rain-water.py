class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = []
        right_max = [0] * len(height)
        maxx_r = maxx_l = 0
        j = len(height) - 1
        for i in range(len(height)) :
            maxx_l = max(maxx_l, height[i])
            maxx_r = max(maxx_r, height[j])
            left_max.append(maxx_l)
            right_max[j] = maxx_r
            j -= 1
        summ = 0
        for i in range(len(height)) :
            summ += min(left_max[i], right_max[i]) - height[i]
        return summ
        
            