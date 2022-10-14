class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket, maxfruits, left = {}, 0, 0
        for right in range(len(fruits)):
            if fruits[right] not in basket:
                basket[fruits[right]] = 0
            
            basket[fruits[right]] += 1
            
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            maxfruits = max(maxfruits, right - left + 1)
        return maxfruits