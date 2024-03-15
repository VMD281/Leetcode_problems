class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        curr_profit = 0
        max_profit = 0
        for i in range(1,n):
            curr_profit += prices[i] -prices [i-1]
            if curr_profit >0:
                pass
            
            else:
                curr_profit = 0
            max_profit = max(max_profit, curr_profit)
        return max_profit


        