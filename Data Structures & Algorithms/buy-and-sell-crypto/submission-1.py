class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #returning the maximum profit
        #we can only buy and sell once, so have to determine on best index to buy and one best index to sell 
        
        #Use a 2 pointer solution. sell and buy.
        #if the next day is lower than current day, then update sell to next day, and buy to next next day.
        #if next day is higher than sell day, then record profit and update buy pointer.
        
        #we will only have to run through the list once so solution is O(n) time and O(1) space.

        profit = 0
        buy, sell = 0, 1

        while sell < len(prices):

            if prices[sell] < prices[buy]:
                buy = sell
            else:
                curr_profit = prices[sell] - prices[buy]
                profit = max(curr_profit,profit)
            sell += 1

        return profit