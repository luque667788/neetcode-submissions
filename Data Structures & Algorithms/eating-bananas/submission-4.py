class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        def k_fits(k):
            t = 0
            for pile in piles:
                import math

                t += math.ceil(pile / k)  # round up needed
            return t <= h

        # min and max range ideal k could be in between
        r = max(piles) 
        l = 1
        last_fit = r
        while  l <= r:
            c = (r+l) // 2
            if k_fits(c):
                last_fit = c
                r = c - 1
            else:
                l = c + 1
        return last_fit
                
                


# do a binary search on K?? 
# like the k max would be the biggest array
# the min one would be 1
# then we try until we actually fail and then we 
# just change the range