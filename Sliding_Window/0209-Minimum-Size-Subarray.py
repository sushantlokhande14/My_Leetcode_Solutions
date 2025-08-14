# leetcode Problem 209: Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/  


# Sliding Window Approach
# Time Complexity: O(n)     
# Space Complexity: O(1) - no extra space used


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Initialize pointers and variables
        L = 0 
        total = 0 
        minLength = float('inf')

        # Iterate through the array with a right pointer
        for R in range(len(nums)): 
            # Add the current element to the total
            total += nums[R]
            # While the total is greater than or equal to the target
            # This means we have a valid subarray that meets the condition  
            # We try to shrink the window from the left
            # to find the minimum length subarray   
            while total >= target: 
                # Update the minimum length if the current window is smaller
                # R - L + 1 gives the current window size   
                # R is the right pointer and L is the left pointer
                # We add 1 because the range is inclusive of L and R
                minLength = min(minLength, R- L + 1)
                # Remove the leftmost element from the total
                # This effectively shrinks the window from the left
                # and allows us to check for smaller valid subarrays        
                total -= nums[L]
                # Move the left pointer to the right
                # This is necessary to continue checking for smaller subarrays  
                L +=1 

        # If minLength was updated, return it; otherwise, return 0
        # If minLength is still infinity, it means no valid subarray was found      
        if minLength == float('inf'): 
            return 0 
        
        else: 
            return minLength 