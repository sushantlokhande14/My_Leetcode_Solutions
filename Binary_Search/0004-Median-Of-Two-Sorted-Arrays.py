# Leetcode 004 - Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Difficulty: Hard

# Brute force solution 
# Time Complexity: O(m+n) where m and n are the lengths of the two arrays
# Space Complexity: O(m+n) for storing the merged array

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)

        merged = nums1 + nums2 
        merged.sort()
        mid = len(merged)//2
        if len(merged)%2 ==0:
             
            res = (merged[mid]+merged[mid-1])/2 
        else: 
            res = merged[mid] 
        return res

