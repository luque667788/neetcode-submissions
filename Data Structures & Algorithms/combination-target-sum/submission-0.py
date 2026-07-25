import copy

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res, sol = [], []
        def dfs(i: int,s: int):

            if s == target:
                res.append(sol.copy())
                return
            elif s > target or  i >= len(nums):
                return # finished but it is not a solution

            # use the two branches 

            # choose to append nums[i]
            sol.append(nums[i])
            dfs(i, s + nums[i])
            sol.pop()
            # we wont append nums[i] any more, go the the next
            dfs(i +1, s)
        dfs(0,0)
        return res            





        