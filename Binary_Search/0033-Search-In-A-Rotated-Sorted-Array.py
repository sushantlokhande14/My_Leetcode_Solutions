# leetcode problem 33: `Search in a Rotated Sorted Array`
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

# brute force
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target: 
                return i  
        return -1 


#Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)-1 
         
        while l<=r: 

            m = (l+r)//2 
            if target == nums[m]:
                return m
            
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1 
                else: 
                    r = m-1 
                
            else: 
                if nums[m]> target or nums[r] < target:
                    r = m - 1
                else : 
                    l = m+1 
            
        return -1 



