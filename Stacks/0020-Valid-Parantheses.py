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

