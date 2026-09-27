class Solution(object):
    def maxProfit(self, prices):

        maxprofit=0
        buyprice= prices[0]

        for n in prices:
            if n > buyprice:
                profit = n - buyprice
                maxprofit = max(profit, maxprofit)

            else:
                buyprice = n

        return maxprofit
             

        