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


# optimal solution using binary search
# Time Complexity: O(log(min(m,n))) where m and n are the lengths of the two arrays
# Space Complexity: O(1)
# MINDDDD FACKKKKKKKKKKKKK

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1