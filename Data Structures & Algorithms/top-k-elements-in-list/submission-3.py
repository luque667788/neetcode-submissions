class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         nums_freqs = {}
         for n in nums:
            nums_freqs[n] = nums_freqs.get(n ,0) + 1

         freq_buckets = [[] for _ in range(len(nums) + 1)]

         for n, f in nums_freqs.items():
            freq_buckets[f].append(n)

         result = []
         for i in range(len(freq_buckets)  -1, -1, -1): 
            for n in freq_buckets[i]:
                    result.append(n)
                    if len(result) >= k:
                        return result