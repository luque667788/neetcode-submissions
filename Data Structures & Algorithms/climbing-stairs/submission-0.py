class Solution:
    def climbStairs(self, n: int) -> int:
        last_two = [1, 1]  # state of the iteration at 2
        for _ in range(2, n + 1, 1):  # start iteration at staircase 2
            s = last_two[0] + last_two[1]  # 2
            last_two[0] = last_two[1]  # 1
            last_two[1] = s  # 2
        return last_two[1]  # return the last step


        