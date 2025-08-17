#  Leetcode Problem 3: Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/ 


# Sliding Window Approach
# Time Complexity: O(n) - single pass through the string        
# Space Complexity: O(min(n, m)) - where n is the length of the string and m is the size of the character set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset= set()
        res = 0 
        l = 0 

        for r in range(len(s)): 
            while s[r] in charset: 
                charset.remove(s[l]) # remove leftmost 
                l+=1 #update left 


            charset.add(s[r])
            res = max(res , len(charset))
        
        return res 

