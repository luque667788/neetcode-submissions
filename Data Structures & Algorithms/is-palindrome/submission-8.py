class Solution:
    def isPalindrome(self, s: str) -> bool:

        h = 0
        t = len(s) -1
        while True:
            h_a =  s[h].isalnum()
            t_a = s[t].isalnum()

            if h_a and t_a:
                 # go to the next comparison

                if s[h].lower() != s[t].lower():
                    return False

                t -= 1
                h += 1
            else:
                # one of the parties is non alphanumeric, remain in the same comparion (pseudo index)
                if not h_a:
                    h += 1
                if not t_a:
                    t -= 1
            if h >= t: #  they will cross always before invalid index (out of bound)
                    return True





