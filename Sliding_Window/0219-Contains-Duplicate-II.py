# Leetcode Problem 219: Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/  

# Brute Force Solution
# Time Complexity: O(n^2)   Tecnhically O(n*k) but k is a constant
# Space Complexity: O(1)

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Checks if there are two identical numbers in the list `nums`
        whose indices differ by at most `k`.

        Args:
            nums (List[int]): List of integers to check.
            k (int): Maximum allowed distance between duplicate indices.

        Returns:
            bool: True if such a pair exists, False otherwise.
        """

        n = len(nums)  # Total number of elements in the list

        # Outer loop: iterate over each index `L`
        for L in range(n):
            # Inner loop: check only the next `k` elements after index `L`
            # `L + 1` → Start checking from the next element after `L`
            # `L + k` → Maximum allowed index for a duplicate (distance <= k)
            # `+1` is needed because range()'s stop value is exclusive
            # `min(n, L + k + 1)` ensures we don't go out of bounds
            for R in range(L + 1, min(n, L + k + 1)):
                # If we find two equal values within the allowed distance
                if nums[L] == nums[R]:
                    return True  # Duplicate found

        # If no such pair is found after checking all possibilities
        return False
    

# Sliding Window Approach
# Time Complexity: O(n) 
# Space Complexity: O(k) - for the hash set

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()  # Sliding window to store last k elements
        L = 0 
        n = len(nums)

        for R in range(n):
            if R - L > k:  # Keep window size at most k
                window.remove(nums[L])
                L += 1 

            if nums[R] in window:  # Duplicate found within k distance
                return True 
            
            window.add(nums[R])  # Add current element to window

        return False  # No duplicates within k distance