import copy

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res,sol = set(),[0] * len(nums)
        def dfs(s):
            if s == target:

                res.add(tuple(sol))
            elif s < target:
                for i in range(len(nums)):
                    sol[i] += 1
                    dfs(s + nums[i])
                    sol[i] -= 1


        dfs(0)

        to_return = []

        for multipliers in res:
            actual_combination = []
            for i,m in enumerate(multipliers):
                for _ in range(m):
                    actual_combination.append(nums[i])
            to_return.append(actual_combination)
        return to_return





'''
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
'''




        