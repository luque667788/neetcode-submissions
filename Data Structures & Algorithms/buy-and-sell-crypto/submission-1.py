class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n*n)
        best = 0
        l = 0
        r = 1
        while r < len(prices):
            profit = prices[r] - prices[l]
            if 0  < profit:
                if best < profit:
                    best = profit
            else: 
                l = r
            r += 1

            
        return best


        