'''
Sliding Window
Sometimes, a problem may ask to return the actual subarray containing the largest sum, instead of just the sum itself. Previously, we didn't have two explicit pointers that kept track of the subarray in the previous implementation but we can actually do this by keeping track of a "window". A window in this case denotes a contiguous subarray that does not break our constraint of the sum staying positive
'''


# Kadane's Algorithm - Sliding Window Approach
# time Complexity: O(n)
# space Complexity: O(1)

