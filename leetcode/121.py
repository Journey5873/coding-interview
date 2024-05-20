class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            profit = prices[i] - min_price
            if max_profit < profit:
                max_profit = profit
            if min_price > prices[i]:
                min_price = prices[i]
        return max_profit
    
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
