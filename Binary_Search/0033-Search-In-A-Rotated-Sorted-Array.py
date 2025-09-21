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
