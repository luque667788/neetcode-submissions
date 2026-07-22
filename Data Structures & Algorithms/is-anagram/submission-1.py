class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first idea, strings chars are integers, i could sort them and then compare both sorted arrays

        # second idea: just search doesnt work unless i brute force search and keep track of combinations
        # set also doest work ince there maybe duplicates

        # third idea would be: iterate and keep track of the occurencies of each char
        # then i can compare the n of occuriencies of each char and then know if they are equal
        # that is probably at max O(n+m) in terms of memory and time would be O(m or n) 
        # another thign is that tha arrays need to be always the same size
        # number of occuries of a char in an string, how to get that in python?
        # for that we can use the Hashtable

        if len(s) != len(t):
            return False
        # assume in python that a hashmap is the same as a dict
        s_char_freqs: Dict = {}
        t_char_freqs:Dict = {}

        for s_char, t_char in zip(s,t):
        
            s_char_freqs[s_char] =  1 + s_char_freqs.get(s_char, 0)
            t_char_freqs[t_char] = 1 + t_char_freqs.get(t_char, 0)
            

        return s_char_freqs == t_char_freqs





        