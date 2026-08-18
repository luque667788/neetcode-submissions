class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best_area = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            w = r - l
            h = 0
            if heights[l] < heights[r]:
                h = heights[l]
                l += 1
            else:
                h = heights[r]
                r -= 1
            area = w * h
            best_area = max(area,best_area)
        return best_area
        

        