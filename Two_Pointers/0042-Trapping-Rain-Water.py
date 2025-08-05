
# LeetCode 42: Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/    
#  This problem can be solved usinng pre-computed arrays for left and right max heights,
# or using a two-pointer approach.


# brute force solution, uses 2 nested loops, time complexity O(n^2), space complexity O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0 
        
        res = 0 

        n = len(height)

        for i in range(n): 
            leftMax = rightMax = height[i]

            for j in range(i):
                leftMax = max(leftMax, height[j])

            for k in range(i+1, n): 
                rightMax = max(rightMax, height[k])

            res += min(leftMax, rightMax) - height[i]

        
        return res


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
# this solution uses two pointers to traverse the array from both ends,
# maintaining the maximum heights seen so far from both sides.  
class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height: 
            return 0 

        l = 0 
        r = len(height)-1 

        leftMax = height[l]
        rightMax = height[r]

        res = 0

        while l < r: 

            if leftMax < rightMax: 

                l+=1 
                leftMax = max(leftMax, height[l])
                res += leftMax- height[l]
            
            else: 

                r-=1 
                rightMax = max(rightMax, height[r])
                res+= rightMax - height[r]

        
        return res 