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


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0 
        l = 0 
        r = len(heights)- 1 

        while l < r : 

            area = (r-l) * min(heights[l], heights[r])

            res = max(area, res)

            if heights[l]< heights[r]: 
                l+=1 
            else: 
                r-=1 

        return res 
        
        