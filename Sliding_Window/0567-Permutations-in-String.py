# Leetcode 0567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/  

# Sliding Window Approach
# Time Complexity: O(n) - single pass through the string    

# Space Complexity: O(1) - since the character set is limited to 26 lowercase letters

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
    
        # Step 1: frequency arrays for s1 and first window of s2
        count1 = [0] * 26
        count2 = [0] * 26
        
        for ch in s1:
            count1[ord(ch) - ord('a')] += 1
        
        for ch in s2[:len(s1)]:
            count2[ord(ch) - ord('a')] += 1
        
        # Step 2: calculate initial matches
        matches = 0
        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1
        
        # Step 3: slide the window
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # character coming in
            index = ord(s2[r]) - ord('a')
            count2[index] += 1
            if count1[index] == count2[index]:
                matches += 1
            elif count1[index] + 1 == count2[index]:
                matches -= 1
            
            # character going out
            index = ord(s2[l]) - ord('a')
            count2[index] -= 1
            if count1[index] == count2[index]:
                matches += 1
            elif count1[index] - 1 == count2[index]:
                matches -= 1
            l += 1
        
        return matches == 26