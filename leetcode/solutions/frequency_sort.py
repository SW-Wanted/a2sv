from typing import List
from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        """
        Contar o numero de frequencia
        [1] = 2
        [2] = 3
        [3] = 1
        -----------------------
        [3] = 1
        [1] = 2
        [2] = 3
        -----------------------
        [3] = 1
        [1] = 2
        [1] = 2
        [2] = 3
        [2] = 3
        [2] = 3
        """

        # freq = dict()
        # el = set(nums)
        # for i in el:
        #     freq[i] = nums.count(i)
        #     nums.remove(i)
        # print(freq)

        # freq = {}
        # for num in nums:
        #     if num in freq:
        #         freq[num] += 1
        #     else:
        #         freq[num] = 1
    
        freq = Counter(nums)
        a = list()
        
        return sorted(nums, key=lambda num: (freq[num], -num))
    # Mandatory
