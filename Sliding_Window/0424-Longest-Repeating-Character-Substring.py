# leetcode Problem 424: Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/       


# Sliding Window Approach
# Time Complexity: O(n) - single pass through the string            
# Space Complexity: O(1) - since the character set is limited to 26 uppercase letters
# Note: The character set is limited to uppercase English letters, so we can use a fixed
# array for counting character frequencies instead of a dictionary.``
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        maxf = 0 
        l = 0 
        for r in range(len(s)): 
            count[s[r]] = 1+ count.get(s[r], 0)
            while (r-l+1) - max(count.values()) > k:

                count[s[l]]-=1 
                l+=1 

            maxf = max(r-l+1 , maxf)

        return maxf
