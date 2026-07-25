class Solution:
    def findMin(self, nums: List[int]) -> int:

        r = len(nums) - 1
        l = 0
        i = r // 2
        # this are the border we are certain the min number is between
        while (
            nums[i - 1] < nums[i]
        ):  # if the num to the left is smaller contiune the search
            if nums[i] < nums[r]:  # nums is smaller then right border
                # then we know nums[i] is the max value we know
                r = i - 1
            else:
                l = i + 1

            i = (r  + l) // 2
        return nums[i]
