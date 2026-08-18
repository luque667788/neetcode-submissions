class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # problem is basically finding the longest 
        # consecutive characters substring that 
        # has a gap of k max in the middle
 
        best_length = 1
        l = 0
        # array index represent the distance to the ascii character a
        # array values represent the frequencies
        char_freqs = [0] * 26
        max_freq = 0

        for r in range(len(s)):
            length_substring = r - l + 1
            # use relative ascii distance from char to A to calculate the index
            # alternative would be using a hashmap
            char_freqs[ ord(s[r]) - ord('A')] += 1

            max_freq = max(char_freqs[ ord(s[r]) - ord('A')], max_freq)

            if (length_substring - max_freq) > k:
                # we reached the limit of gaps
                # need to then move the left pointer to the next, decreasing the size of 
                # the substring
                # and remove that char from the counting of char_freqs in the substring
                char_freqs[ ord(s[l]) - ord('A')] -= 1
                l += 1

            else:
                # valid substring and should attempt next
                best_length = max(best_length, length_substring)


        return best_length
            


        