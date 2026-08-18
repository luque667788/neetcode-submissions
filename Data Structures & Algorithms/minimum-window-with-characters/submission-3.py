class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # frequency counter or something like that
        # sliding window
        # the only problem is to actually figure out the conditoin
        # that triggers the window to decrease
        # could be if any char freq is bigger then what it needs
        # to be, that would be the ideal i guess

        needed_freqs = {}
        for c in t:
            needed_freqs[c] = 1 + needed_freqs.get(c,0)
        substring_char_freqs = {}
        l = 0
        to_return = ""
        shortest_lenght = len(s)
        have = 0
        need = len(needed_freqs.keys())
        for r in range(len(s)):
            freq_current = 1 + substring_char_freqs.get(s[r],0)
            substring_char_freqs[s[r]] = freq_current

            if needed_freqs.get(s[r],-1) == freq_current:
                have += 1

            while True:
                # means substring is complete and it is a candidate for 
                # shortest substring
                if have == need:
                    if r - l < shortest_lenght:
                        shortest_lenght = r - l
                        to_return = s[l:r + 1]

                    substring_char_freqs[s[l]] -= 1
                    if s[l] in needed_freqs:
                        # we just removed on char that was needed
                        # have to check again if it now is too small or something
                        if substring_char_freqs[s[l]] < needed_freqs[s[l]]:
                            have -= 1
                    l += 1
                else:
                    break
                    # go to next iteration, increase the r
        return to_return
            


        