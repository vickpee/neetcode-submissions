class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for i in range(1, len(prices)):
            maybeBuy = prices[i - 1]
            sell = prices[i]
            
            if maybeBuy < buy:
                buy = maybeBuy
            
            if sell - buy > profit:
                profit = sell - buy
        
        return profit