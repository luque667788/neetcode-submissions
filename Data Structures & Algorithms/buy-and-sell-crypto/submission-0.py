class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n*n)
        best = 0
        for day, buy in enumerate(prices[:-1]):
            for sell in prices[day + 1:]:
                profit = sell - buy
                if best < profit:
                    best = profit
        return best





        