class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        number_of_boats = 0
        left = 0
        right = len(people) - 1

        while left <= right:
            remain = limit - people[right] # heaviest person
            right -= 1

            if people[left] <= remain:
                left += 1
            number_of_boats += 1

        return number_of_boats