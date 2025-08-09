# leetcode problem 0739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/ 

# brute force solution
# Time complexity O(n^2), space complexity O(1)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = []
        n = len(temperatures)

        for i in range(n): 
            counter = 0 
            for j in range(i+1,n): 
                if temperatures[j] > temperatures[i]: 
                    result.append(counter)
            
                else: 
                    counter+=1 

        return result  
            