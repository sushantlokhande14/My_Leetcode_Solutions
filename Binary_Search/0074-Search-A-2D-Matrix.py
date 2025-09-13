# leetcode 0074 Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/



# Brute Force
# Time Complexity: O(m*n)
# Space Complexity: O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in range(len(matrix)): 
            for c in range(len(matrix[0])):
                if matrix[r][c] == target: 
                    return True 

        return False 