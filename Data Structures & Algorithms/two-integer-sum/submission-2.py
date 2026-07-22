class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # plan here
        # brute force??
        # sort?
        # sort and then sliding window?

        # get the smaller number, try to sum it up

        # find the lcms?
        # itreate with biggest number (that is smaller then target)
        # from smalles number, like a sliding window

        # idea. make a hashset out of list

        # then iterate through the list subtraction targer - current item
        # then trying to see if the hasmap has a that item.
        # problem (edge case), target/2 = current item,

        # have to find a way to exclude that? but then the set solution woulndt workt becasue we
        # actaualy it needs to be a hashmap becasue we need to know also the index of it.

        # but then we come back to the problem if there are duplicate values on the array
        # since this would be problematic
        value_index_map = {}
        for i, n in enumerate(nums):
            w = target - n

            if w in value_index_map:
                return sorted([i, value_index_map[w]])
            else:
                value_index_map[n] = i