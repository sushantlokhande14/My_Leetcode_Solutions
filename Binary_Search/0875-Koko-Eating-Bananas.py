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
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res