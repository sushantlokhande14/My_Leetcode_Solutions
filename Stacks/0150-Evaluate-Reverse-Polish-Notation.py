# Leetcode 0150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/   

# This solution uses a stack to evaluate the expression in Reverse Polish Notation (RPN)
# The stack is used to store numbers, and when an operator is encountered,  

# the top two numbers are popped from the stack, the operation is performed,
# and the result is pushed back onto the stack.                                       

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens: 
            if c =="+":
                stack.append(stack.pop() + stack.pop())
            elif c =="*":
                stack.append(stack.pop() * stack.pop())
            elif c =="-":
                a , b = stack.pop() , stack.pop()
                stack.append(b-a) 
            elif c =="/":
                a , b = stack.pop() , stack.pop()
                stack.append(int(b/a))
            else: 
                stack.append(int(c))

        return stack[-1]
