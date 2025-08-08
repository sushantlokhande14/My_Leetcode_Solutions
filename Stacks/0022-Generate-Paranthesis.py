# Leetcode 0022. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/       


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        #to store result 
        res = []
        stack = []

        def backtrack(openN, closedN):
            if openN == closedN == n : 
                res.append("".join(stack))
                return 

            if openN < n : 
                stack.append('(')
                backtrack(openN+1 , closedN)
                stack.pop()

            if openN > closedN: 
                stack.append(")")
                backtrack(openN , closedN+1)
                stack.pop()

        backtrack(0,0)
        return res