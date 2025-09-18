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


# Optimal Approach: Binary Search
# Time Complexity: O(n*log(max(piles)))
# Space Complexity: O(1)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles)
        res = max(piles)

        while l<=r: 
            hours = 0 
            k = (l+r)//2

            for pile in piles: 
                hours += math.ceil(pile/k)

            if hours<=h : 
                res = min(res, k)
                r = k - 1
            
            else: 
                l = k +1 
        
        return res 