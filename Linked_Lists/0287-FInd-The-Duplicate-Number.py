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


# Floyd's Tortoise and Hare (Cycle Detection)
# time complexity O(N) where N is total number of nodes in all the lists
# space complexity O(1) because we are not using any extra space


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        fast ,slow = 0,0 

        while True : 
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow : 
                break 


        slow2 = 0  
        while True : 
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2: 
                return slow


        return -1 
