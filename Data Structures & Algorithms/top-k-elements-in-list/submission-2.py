class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         # hashmaps are good to track frequency since they are O(n)
         # then i need to sort the array (or reverse sort it)
         # and then get the last k elements or first elements of it 


        n_f = defaultdict(int) # default value is 0
         # Hashmap is O(n) space complexity

        for n in nums:
            n_f[n] = n_f[n] + 1
        
        f_n = defaultdict(list)

        for n,f in n_f.items():
            f_n[f].append(n)
                

        # i want to rank by the frequency (value) but then return the key (number)
        # sort is time complexity O(nlogn) -> problem??
        _a = reversed(sorted(f_n.keys()))

        top_frequent_numbers = []
        for key in _a:
            for n in f_n[key]:
                top_frequent_numbers.append(n)
                if len(top_frequent_numbers) == k:
                    return top_frequent_numbers