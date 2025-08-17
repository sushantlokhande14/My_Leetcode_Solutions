# Leetcode 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/    


# Brute Force Approach
# Time Complexity: O(n^2) - nested loops to check all pairs
# Space Complexity: O(1) - no extra space used

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0 
        n = len(prices)

        for i in range(n): 
            for j in range(i+1 , n ): 
                prof = prices[j] - prices[i]

                maxProf = max(prof, maxProf)
        
        return maxProf
    
# Sliding Window Approach
# Time Complexity: O(n) - single pass through the array 
# Space Complexity: O(1) - no extra space used

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0 
        sell = buy + 1 
        maxProf = 0 


        while sell < len(prices): 

            if prices[sell] > prices[buy] : 
                profit = prices[sell] - prices[buy]
                maxProf = max(maxProf, profit)
            else: 
                buy = sell 
            
            sell +=1 

        return maxProf
    
    