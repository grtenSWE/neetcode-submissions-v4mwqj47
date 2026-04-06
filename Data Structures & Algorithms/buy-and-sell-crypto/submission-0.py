class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #returning the maximum profit
        #we can only buy and sell once, so have to determine on best index to buy and one best index to sell 
        profit = 0
        for day in range(len(prices)-1):
            best = max(prices[day:])
            curr_profit = best - prices[day]
            if profit < curr_profit and curr_profit > 0:
                profit = curr_profit

        return profit
        