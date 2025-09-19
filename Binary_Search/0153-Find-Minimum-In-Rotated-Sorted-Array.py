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
# This approach works because in a rotated sorted array, one half of the array is always sorted. By comparing the middle element with the leftmost and rightmost elements, we can determine which half contains the minimum element and narrow our search accordingly.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums)-1 

        res = float("inf")
        while l<=r: 

            if nums[l]< nums[r]:
                res = min(res, nums[l])
                break

            m = (l+r)//2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1 
            else: 
                r = m-1 
            
        return res 
    
# optional 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]