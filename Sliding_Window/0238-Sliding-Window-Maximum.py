# Leetcode 0238. Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum


# Brute Force Approach
# Time Complexity: O(n*k) - where n is the length of nums and k is
# the size of the sliding window
# Space Complexity: O(1) - no extra space used


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # bruteforce 

        output = []
        n = len(nums)
        maxi = float("-inf")
        for i in range(n -k + 1 ): 
            maxi = nums[i]
            for j in range(i, i+k): 
                maxi = max(maxi, nums[j])
            output.append(maxi)

        
        return output 