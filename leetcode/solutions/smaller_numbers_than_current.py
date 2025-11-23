from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a = []
        c = 0
        n = range(len(nums))
        sort = sorted(nums)
        for i in n:
            for j in n:
                if nums[i] == sort[j]:
                    break;
                c += 1
            a.append(c)
            c = 0
        return a;
# Mandatory
