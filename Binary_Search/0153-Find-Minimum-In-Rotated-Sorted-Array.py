# Leetcode 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


# brute force
# Time Complexity: O(n)
# Space Complexity: O(1)

# This approach works because the array is guaranteed to be rotated, meaning there is at least one point where the order breaks. By iterating through the array and checking for this break, we can find the minimum element efficiently.
class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums)-1): 
            if nums[i+1]< nums[i]:
                return nums[i+1]
        return nums[0]
    
#brute force 2 
# Time Complexity: O(nlogn)
# Space Complexity: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        return nums[0]
    
# brute force 3 
# Time Complexity: O(n)
# Space Complexity: O(1)
# This approach works because the minimum element in a rotated sorted array is the smallest element, which can be found by simply iterating through the array and keeping track of the minimum value encountered.
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
    

# Optimal Approach: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)


