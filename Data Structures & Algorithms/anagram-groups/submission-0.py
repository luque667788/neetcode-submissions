class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strategy would be make char frequency maps for each str in the List
        # then the next step would be
        # compare the ones that are the same and group them together
        # but how to group them together? brute force match compare?
        # need a way to have a hasmap of hasmaps??
        # like the key is the hasmap freqs and the
        # that gives O(n * m) time complexity
        anagrams = {}
        for string in strs:
            _chars_freq = {}
            for char in string:
                _chars_freq[char] = _chars_freq.get(char, 0) + 1

            # problem: we cannot use dict as key for a dict in python
            # we could use a sorted tuple, since tuples can have repeated values
            _keypairs = []
            for key, value in _chars_freq.items():
                _keypairs.append((key, value))
            hashablekey = tuple(sorted(_keypairs))

            _a = anagrams.get(hashablekey, [])
            _a.append(string)

            anagrams[hashablekey] = _a
        # flatten the hashmap
        to_return = []
        for substrings in anagrams.values():
            to_return.append(substrings)
        return to_return
