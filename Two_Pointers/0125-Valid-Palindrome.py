# Solution - Easy way - Builtin functions using slicing O(n), O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum(): 
                newStr += c.lower()
        return newStr == newStr[::-1]
        

# solution using Two pointers - constant space , Use two pointers , left and right 

class Solution: 

    def  isalphanumeric(self, c): 
        return (ord('A')<= ord(c)<= ord('Z') or
                ord('a')<= ord(c)<= ord('z') or 
                ord('0')<= ord(c)<= ord('9'))

    def isPalindrome(self, s: str) -> bool:

        l = 0 
        r = len(s) -1 

        while l < r : 
            
            while l< r and not self.isalphanumeric(s[l]): 
                l+=1 
            while r>l and not self.isalphanumeric(s[r]): 
                r-=1 

            if s[l].lower() != s[r].lower():
                return False 
            
            l += 1 
            r -= 1 

        return True 
