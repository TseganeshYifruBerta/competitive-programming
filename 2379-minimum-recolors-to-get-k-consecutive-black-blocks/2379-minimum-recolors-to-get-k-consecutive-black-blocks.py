class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        dictionary = defaultdict(int)
        min_opr = inf
        for right in range(len(blocks)):
            dictionary[blocks[right]] += 1
            if right - left + 1 == k:
                min_opr = min(dictionary['W'], min_opr)
                dictionary[blocks[left]] -= 1
                left += 1
        if right - left + 1 == k:
            min_opr = min(dictionary['W'], min_opr)
        return min_opr