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
            

# Optimized solution using stack
# Time complexity O(n), space complexity O(n)   

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)  # Total number of days
        res = [0] * n          # Initialize result list with 0s for each day
        stack = []             # Stack to store (temperature, index)

        # Iterate through each day's temperature with its index
        for curr_day, curr_temp in enumerate(temperatures): 
            
            # Check if current temperature is warmer than the top of the stack
            while stack and curr_temp > stack[-1][0]:
                prev_temp, prev_day = stack.pop()     # Pop the last colder day
                res[prev_day] = curr_day - prev_day   # Compute how many days to wait

            # Add the current day and temperature to the stack
            stack.append((curr_temp, curr_day))

        # Any remaining days in the stack don't have a warmer future temperature,
        # so their result stays as 0 (already initialized that way).
        return res
