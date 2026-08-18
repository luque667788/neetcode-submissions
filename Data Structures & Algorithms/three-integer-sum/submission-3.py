class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        to_return = []
        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            a = nums[i]

            want = -a
            l, r = i + 1, len(nums) - 1

            # two  pointer search
            while l < r:
                b = nums[l]
                c = nums[r]
                s = b + c
                if s == want:
                    to_return.append([a, b, c])
                    r -= 1
                    l += 1
                    # move both pointers since eeach number can only be summed up 
                    # to a certain sum with that exact other number
                    # so if we want another possible result both numbers will actually  
                    # have to change
                    # just make sure there are no duplicates 
                    # which will make the result repeat itself (find next different number)
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < want:
                    l += 1
                else:
                    r -= 1
        return to_return
