
# LeetCode 42: Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/    
#  This problem can be solved usinng pre-computed arrays for left and right max heights,
# or using a two-pointer approach.
#


# Sub optimal- Solution using pre-computed arrays, time complexity O(n), space complexity O(n) 

class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)

        leftMax = [0]*n 
        rightMax = [0]*n 

        leftMax[0] = heights[0]
        for i in range(1 , n): 
            leftMax[i] = max(leftMax[i-1], heights[i])

        rightMax[n-1] = heights[n-1]
        for i in range(n-2, -1,-1):
            rightMax[i] = max(rightMax[i+1],heights[i])

        
        res = 0 
        for i in range(n):
            res += min(leftMax[i], rightMax[i])- heights[i]

        return res
    
# Optimized solution using two pointers, time complexity O(n), space complexity O(1)