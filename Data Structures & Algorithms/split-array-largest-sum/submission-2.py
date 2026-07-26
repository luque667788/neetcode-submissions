class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def can_split(target: int):
            sumsubstring = 0
            n_substring = 1 # always have one array at least
            for n in nums:
                sumsubstring += n
                if sumsubstring > target:
                    # end current substring and start a new one at n
                    sumsubstring = n
                    n_substring += 1
                    # problem here is on the last iteration that wont work
                    # since we would add basically an extra substring
            return n_substring <= k

        _max= sum(nums)
        _min = max(nums)
        while _min <= _max:
            _current = (_max + _min) // 2
            if can_split(_current):
                _max = _current - 1
            else:
                _min = _current + 1
            
        return _min
        