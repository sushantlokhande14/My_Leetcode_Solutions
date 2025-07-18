class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mapp = {}

        for i, num in enumerate(nums):
            diff = target - num 

            if diff in mapp.keys():
                return [mapp[diff],i]

            else: 
                mapp[num]= i 
