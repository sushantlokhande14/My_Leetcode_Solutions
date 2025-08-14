# Leetcode 53 Problem: Maximum Subarray

'''
# Problem Statement:
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
'''

# Kadane's ALgorithm - Brute Force Approach 
# time Complexity: O(n^2)
# space Complexity: O(1)    

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]

        for i in range(len(nums)): 
            currSum = 0 
            for j in range(i , len(nums)): 
                currSum += nums[j]
                maxSum = max(currSum, maxSum)


        return maxSum
    
# Optmal Approach - Kadane's Algorithm using sliding window, dynamic programming
# time Complexity: O(n) 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0 

        for n in nums: 
            curSum = max(curSum , 0 )
            curSum += n 
            maxSum = max(curSum , maxSum)

        return maxSum   
