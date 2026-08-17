class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = len(nums)

        l, r = 0, s - 1 

        while l <= r:
            i = (r + l) // 2

            if target == nums[i]:
                return i

            # for every index in the array there is only two options:
            # either it is in the sorted part of the array to the left
            # it is in the other sorted part of the array to the right

            if  nums[l] <= nums[i]:
                # means everything to the left is smaller

                if  nums[l] <= target < nums[i]: 
                    # it fits the range, go left
                    r = (i - 1)
                else: # not to the left, go search further right
                    l = i + 1

            elif nums[i] < nums[r]:
                # everything to the right is bigger

                    if nums[i] < target <= nums[r]:
                        # it fits the range, go right
                        l = i + 1
                    else:  # not in the right side, go search in the left
                        r = i - 1


            
        return -1

        