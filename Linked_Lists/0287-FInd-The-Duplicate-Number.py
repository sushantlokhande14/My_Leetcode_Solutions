#  Leetcode  287. Find the Duplicate Number
#  https://leetcode.com/problems/find-the-duplicate-number/ 

# brute force
# time complexity O(NlogN) where N is total number of nodes in all the lists
# space complexity O(N) for storing all the nodes in a list

# the solution is NLOGN because we are sorting the list of nodes
# and sorting takes NLOGN time  
# and we are doing this for N nodes

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)): 
            if nums[i] == nums[i+1]: 
                return nums[i]
            

# Hashmap solution
# time complexity O(N) where N is total number of nodes in all the lists
# space complexity O(N) for storing all the nodes in a hashmap

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for i in nums: 
            if i in seen: 
                return i 
            seen.add(i)
