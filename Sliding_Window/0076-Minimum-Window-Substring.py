# Leetcode 0076. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/   

# Sliding Window Approach
# Time Complexity: O(n) - single pass through the string
# Space Complexity: O(m) 

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =="": 
            return "" 

        countT = {} #Fixed size 
        window = {} # Variable Window 

        for c in t: 
            countT[c] = 1 + countT.get(c, 0)

        l = 0 # left pointer
        res = [-1,-1] #Array to store the left and right indices of the result  
        resLen = float("inf") # since we go for minimum we selected the infinity
        have = 0 # initial count of haves 
        need = len(countT) # returns the number of keys 

        # loop thorugh the right pointer 
        for r in range(len(s)): 

            #add the character to the hashmap window 
            c = s[r]
            window[c] = 1+ window.get(c,0)

            # check if satified 
            if c in countT and window[c] == countT[c] : 
                have +=1 

            #if condition met we update the window to find more smaller options
            while have == need: 

                #update the res 
                if (r-l+1 ) < resLen: 
                    res = [l,r]
                    resLen = r-l+1 

                #shrink window from left 
                window[s[l]] -= 1 

                # if we took out one from an already satisfied , decrement 
                if s[l] in countT and window[s[l]] <countT[s[l]]: 
                    have -=1

                
                l+=1
        
     
        l = res[0]
        r = res[1]

        if resLen == float("inf"): 
            return "" 
        else: 
            return s[l:r+1]
                
