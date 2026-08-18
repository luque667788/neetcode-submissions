class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        a_seen = set()
        to_return = []
        for i in range(len(nums) - 2):
            a = nums[i]
            if a not in a_seen:
                a_seen.add(a)
                want = -a
                l,r = i + 1,len(nums) - 1
                
                # two  pointer search
                while l < r:
                    b = nums[l]
                    c = nums[r]
                    s = b + c
                    if s == want:
                        to_return.append([a,b,c])

                    if s < want:
                        # skip duplicates
                        while l < len(nums) and nums[l] == nums[l + 1]:
                            l += 1
                        
                        l += 1
                    else:
                        # skip duplicates
                        while r > 0 and nums[r] == nums[r - 1]:
                            r -= 1

                        r -= 1

        return to_return






        