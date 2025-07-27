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
