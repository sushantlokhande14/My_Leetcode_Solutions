# Leetcode 004 - Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Difficulty: Hard

# Brute force solution 
# Time Complexity: O(m+n)log(m+n) where m and n are the lengths of the two arrays
# Space Complexity: O(m+n) for storing the merged array

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        merged = nums1 + nums2 
        merged.sort()
        mid = len(merged)//2
        if len(merged)%2 ==0:
             
            res = (merged[mid]+merged[mid-1])/2 
        else: 
            res = merged[mid] 
        return res

# solution using two pointers
# Time Complexity: O(m+n) where m and n are the lengths of the two arrays
# Space Complexity: O(m+n) for storing the merged arraay


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0 
        j = 0 
        merged = []

        while i <= len(nums1)-1 and j <= len(nums2)-1:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i+=1 
            else: 
                merged.append(nums2[j])
                j+=1 
        # one of the arrays exhausted 
        while i<=len(nums1)-1:
            merged.append(nums1[i])
            i+=1 
            
        while j <= len(nums2)-1:
            merged.append(nums2[j])
            j+=1 
            

        mid = len(merged)//2 
        if len(merged)%2 == 0 : 
            res = (merged[mid-1]+ merged[mid])/2
        else: 
            res = merged[mid]
        
        return res 
