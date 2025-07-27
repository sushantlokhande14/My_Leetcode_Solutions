#Solution 1 - Brute Force - double for loop , exploring all combinations ... time complexity O(n^2) and space O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)): 
            product = 1
            for j in range(len(nums)): 
                if i==j: 
                    continue 
                else: 
                    product = product*nums[j]
            
            res.append(product)
        
        return res

#Solution using prefix and postfix - time complexitey O(n) space O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        pre = [0]*n
        suf = [0]*n

        pre[0]= 1
        suf[n-1]= 1

        for i in range( 1, n): 
            pre[i] = nums[i-1]*pre[i-1 ]

        for i in range(n-2, -1,-1):
            suf[i] = nums[i+1] * suf[i+1]

        for i in range(n):
            res[i] = pre[i]* suf[i]

        return res
