import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         nums_freqs = {}
         for n in nums:
            nums_freqs[n] = nums_freqs.get(n ,0) + 1

         heap = []
         for n, f in nums_freqs.items():
            if len(heap) < k:
               heapq.heappush(heap,(f,n))
            else:
               heapq.heappushpop(heap,(f,n))

         freq_buckets = heap
         result = []
         for i in range(len(freq_buckets)): 
            result.append(freq_buckets[i][1])
         return result