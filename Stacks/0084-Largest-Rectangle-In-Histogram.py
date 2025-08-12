# Leetcode 84. Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/



class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Initialize a variable to keep track of the maximum rectangle area found
        maxArea = 0 
        
        # Initialize an empty stack to store tuples of (start index, height)
        # The stack helps in tracking increasing bars and calculating area when we find a shorter bar
        stack = []  # Example: [(index, height)]

        # Loop through each bar in the histogram along with its index
        for i, h in enumerate(heights):
            # Assume the current bar starts at index i
            # This may change if we pop taller bars and find we can extend this bar further back
            start = i 

            # While the stack is not empty AND the current height is less than the height of the bar on top of the stack
            # This means the current bar breaks the increasing sequence — we have to compute area for taller bars
            while stack and stack[-1][1] > h:
                # Pop the last bar from the stack (i.e., the taller bar that can no longer extend to the right)
                index, height = stack.pop()

                # Calculate area: the height is fixed, width is from the popped index to current i
                area = height * (i - index)

                # Update the maximum area if this is the largest we've seen so far
                maxArea = max(maxArea, area)

                # Update start — because the current (shorter) bar can potentially extend back to this popped bar's start
                start = index

            # After popping, push the current bar to the stack with its start index (could be original i or further back)
            # We store the earliest possible start index to ensure we cover the full width next time this bar is popped
            stack.append((start, h))
        
        # Now we've processed all bars, but the stack might still contain bars
        # These bars are part of a non-decreasing sequence till the end of the histogram
        for i, h in stack:
            # For each bar, since no shorter bar came after it, its width extends till the end of the histogram
            width = len(heights) - i

            # Calculate the area for this bar and update maxArea if needed
            maxArea = max(maxArea, h * width)

        # Finally, return the maximum area found
        return maxArea