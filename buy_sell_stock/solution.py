class Solution:
    def maxProfit(self, prices) -> int:
        # Set initial profit variable to zero to be used later for determining maximum profit.
        maxProfit = 0
        n = len(prices)
        
        for i in range(n):
            # If first member in the price list, set this to the temporary minimum variable.
            if i == 0:
                tempMin = prices[i]
            # Find the minimum based on current iteration, either the temp minimum or the current list member.
            minPrice = min(tempMin, prices[i])
            # Set new minimum value to temporary minimum for next iteration of loop.
            tempMin = minPrice
            # Check to see if current list element minus the minimum gives a new maximum; if so, set equal to maxProfit.
            if prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
        
        # Return maximum profit, or return 0 if there is no maximum
        if maxProfit > 0:
            return maxProfit
        
        return 0