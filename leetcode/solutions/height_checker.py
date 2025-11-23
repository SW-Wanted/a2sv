from typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        # for i in range(len(heights)):
        #     c += 1 if heights[i] != expected[i] else 0
        # return c
        return sum(h1 != h2 for h1, h2 in zip(heights, expected))
    # Mandatory
