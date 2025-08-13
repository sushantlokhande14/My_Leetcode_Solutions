'''
Sliding Window
Sometimes, a problem may ask to return the actual subarray containing the largest sum, instead of just the sum itself. Previously, we didn't have two explicit pointers that kept track of the subarray in the previous implementation but we can actually do this by keeping track of a "window". A window in this case denotes a contiguous subarray that does not break our constraint of the sum staying positive
'''


# Kadane's Algorithm - Sliding Window Approach
# time Complexity: O(n)
# space Complexity: O(1)

# initializations 

def max_subarray_indices(nums):
    curSum = 0
    maxSum = nums[0]
    L = 0  # left pointer for current window
    maxL = 0
    maxR = 0

    for R in range(len(nums)):
        if curSum < 0:
            curSum = 0
            L = R  # reset window start

        curSum += nums[R]  # accumulate sum

        if curSum > maxSum:
            maxSum = curSum
            maxL = L
            maxR = R

    return [maxL, maxR], maxSum  # return both indices and max sum


# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
indices, max_sum = max_subarray_indices(nums)
print(f"Max subarray indices: {indices}, Max sum: {max_sum}")