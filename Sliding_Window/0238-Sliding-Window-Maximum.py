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
    

# Optimized Approach using Deque
# Time Complexity: O(n) - each element is added and removed from the deque at most
# once
# Space Complexity: O(k) - the deque can store at most k elements


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0 
        r = 0 
        q = collections.deque()
        res = []

        while r < len(nums): 

            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if l > q[0]: 
                q.popleft()
            
            if r+1 >= k : 
                res.append(nums[q[0]])
                l+=1 
            
            r+= 1 

        return res 
