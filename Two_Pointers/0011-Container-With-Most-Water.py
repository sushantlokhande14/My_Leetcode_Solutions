# Brute force solution, uses 2  nested loops, time complexity O(n^2), space complexity O(1)


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        res = 0 
        for i in range(len(heights)): 
            for j in range(i+1 , len(heights)): 
                area =( min(heights[i] , heights[j])* (j-i)) 

                res = max(res, area)

        return res 
    

# Optimized solution using two pointers, time complexity O(n), space complexity O(1)
