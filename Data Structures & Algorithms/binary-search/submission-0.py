class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bin_search(nums, target):
            r = len(nums) - 1
            l = 0
            
            while l <=  r:
                mid = (l + r) // 2
                value = nums[mid]

                if value < target:
                    l = mid + 1
                elif value > target:
                    r = mid - 1
                elif value == target:
                    return mid
            return -1

        return bin_search(nums, target)

                
                

        