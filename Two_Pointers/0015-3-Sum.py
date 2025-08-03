# brute force solution , uses triple nested loops , time complexity O(n^3), space complexity O(1) 


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)
        nums.sort()

        for i in range(n): 
            for j in range(i+1,n): 
                for k in range(j+1, n): 
                    if nums[i] + nums[j]+ nums[k]== 0: 
                        res.add(tuple([nums[i],nums[j],nums[k]]))

        return [list(i) for i in res ] 
    


# Optimized solution using two pointers, time complexity O(n^2), space complexity O(1)