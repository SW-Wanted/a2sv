class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for start, end in zip(l, r):
            subarray = nums[start:end + 1]
            subarray.sort()
            if len(subarray) < 2:
                result.append(True)
                continue
            difference = subarray[1] - subarray[0]
            is_arithmetic = True
            for i in range(2, len(subarray)):
                if subarray[i] - subarray[i - 1] != difference:
                    is_arithmetic = False
                    break
            result.append(is_arithmetic)
        return result