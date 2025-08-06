# LeetCode Problem: Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/ 

# Brute Force solution for valid parentheses, time complexity O(n^2), space complexity O(1)

class Solution:
    def isValid(self, s: str) -> bool:
        # Keep removing matching pairs of parentheses, braces, or brackets
        while '()' in s or '{}' in s or '[]' in s:
            # Remove all instances of "()" from the string
            s = s.replace('()', '')
            # Remove all instances of "[]" from the string
            s = s.replace('[]', '')
            # Remove all instances of "{}" from the string
            s = s.replace('{}', '')

        # If the string is empty after all valid pairs are removed, it's valid
        if s == '':
            return True

        # If anything is left, it means the brackets were not balanced
        return False

# optimal solution using stack, time complexity O(n), space complexity O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        
        # Initialize an empty stack to keep track of opening brackets
        stack = []

        # Create a mapping of closing brackets to their corresponding opening brackets
        mapper = {")": "(", "]": "[", "}": "{"}

        # Iterate through each character in the input string
        for c in s:
            # If the character is a closing bracket
            if c in mapper:
                # Check if the stack is not empty and the top of the stack matches the corresponding opening bracket
                if stack and stack[-1] == mapper[c]:
                    stack.pop()  # Valid match found, remove the opening bracket from the stack
                else:
                    return False  # Either the stack is empty or brackets don't match
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(c)

        # If the stack is empty at the end, all brackets matched correctly
        if not stack:
            return True

        # If the stack is not empty, some brackets were not closed properly
        return False