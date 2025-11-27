from functools import cmp_to_key

class Solution:
    def compare(a: str, b: str) -> int:
            if a + b < b + a:
                return 1
            elif a + b > b + a:
                return -1
            else:
                return 0
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))
        nums_str.sort(key=cmp_to_key(Solution.compare))
        largest_num = ''.join(nums_str)
        return '0' if largest_num[0] == '0' else largest_num