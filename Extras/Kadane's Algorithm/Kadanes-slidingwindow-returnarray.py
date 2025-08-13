'''
Sliding Window
Sometimes, a problem may ask to return the actual subarray containing the largest sum, instead of just the sum itself. Previously, we didn't have two explicit pointers that kept track of the subarray in the previous implementation but we can actually do this by keeping track of a "window". A window in this case denotes a contiguous subarray that does not break our constraint of the sum staying positive
'''


# Kadane's Algorithm - Sliding Window Approach
# time Complexity: O(n)
# space Complexity: O(1)

# initializations 

curSum = 0 
maxSum = nums[0]
maxL = 0 
maxR = 0 


for R in range(len(nums)): 
    if curSum < 0 :
        curSum = 0 
        L = R 

    curSum = nums[R]
    
    if curSum > maxSum : 
        maxSum = curSum 
        maxL = L 
        maxR = R 

return [maxL, maxR ]