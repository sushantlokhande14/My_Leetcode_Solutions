# Leetcode 0155. Minimum Stack
# https://leetcode.com/problems/min-stack/    


# This is an optimal solution using another stack to keep track of the minimum element
# The main stack holds all the elements, while the minstack keeps track of the minimums
# This allows us to retrieve the minimum element in constant time
# Time complexity is O(1) for push, pop, top, and getMin operations

class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack= []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack: 
            self.minstack.append(min(val, self.minstack[-1]))
        else: 
            self.minstack.append(val)
        

    def pop(self) -> None:
        self.minstack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
   