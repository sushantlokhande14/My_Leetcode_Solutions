# Leetcode 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/

# Brute Force
# Time Complexity: O(n*max(piles))
# Space Complexity: O(1)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 1
        while True: 
            total_time = 0 
            for pile in piles: 
                total_time += math.ceil(pile/speed)

            if total_time <= h: 
                return speed 
            
            speed+= 1 

        return speed