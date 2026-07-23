class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        # get the next non alpha numeric number on a string starting from an index i (inclusive)
        # returns None if there is no next alpha numeric eleent in the direction of the step
        # if i is alnum it return i
        def next_alnum_i_in_string(string: str, i: int, step: int) -> Optional[int]:

            if 0 <= i < len(string):
                if not string[i].isalnum():
                    return next_alnum_i_in_string(string, i + step , step)
                else:
                    return i
            else:
                return None

        h = 0
        t = len(s) -1
        while True:
            n_h = next_alnum_i_in_string(s, h, 1)
            n_t = next_alnum_i_in_string(s, t, -1)

            if n_h is None or n_t is None:
                return True
            else:
                h = n_h
                t = n_t

            # problem what if the next is also non alpha?
            if s[h].lower() != s[t].lower():
                print(f"head: {s[h]} and the tail is:{s[t]}")
                return False
            t -= 1
            h += 1



